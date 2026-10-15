# HTTPS en la red local del hotel (`horus.com`)

Cómo poner un servidor web interno con `https://` y que **todos los puestos lo abran con el candado, sin avisos**, usando una autoridad de certificación (CA) propia del hotel.

> **¿Es un certificado «falso»?** No en sentido técnico: es un certificado real, firmado por una CA real… pero **privada**. Solo la reconocen los equipos donde instales la CA. Fuera del hotel no vale para nada, y eso es justo lo que queremos.

## Cómo funciona

```
 ┌──────────────────────┐   firma    ┌──────────────────────────┐
 │ CA interna del hotel │ ─────────► │ Certificado del servidor │  ← va en el servidor web
 │  HorusCA.key (secreta│            │  horus.com.crt + .key    │
 │  HorusCA.crt (pública)            └──────────────────────────┘
 └──────────┬───────────┘
            │ se instala SOLO la parte pública (HorusCA.cer / .crt)
            ▼
   Puestos de trabajo: Windows · Linux · macOS · móviles
```

1. Generas la CA y el certificado del servidor **en el propio servidor** con `generar_certificados.sh`.
2. Configuras el servidor web con su certificado.
3. Haces que `horus.com` apunte a la IP del servidor dentro de la red (DNS).
4. Instalas la CA (solo su parte pública) en cada puesto.

## Archivos de esta carpeta

| Archivo | Para qué |
|---|---|
| `generar_certificados.sh` | Crea la CA (una vez) y el certificado del servidor. También sirve para renovarlo. |
| `instalar_ca_windows.bat` | Instala la CA en un puesto Windows (y la activa en Firefox). |
| `instalar_ca_linux.sh` | Instala la CA en un puesto Linux (sistema, Chrome/Chromium y Firefox). |
| `anadir_hosts_windows.bat` / `anadir_hosts_linux.sh` | Sin acceso al DNS: hacen que `horus.com` apunte al servidor en cada puesto. |
| `.gitignore` | Impide que las claves generadas acaben en el repositorio. |

---

## 0. Antes de empezar: el nombre del servidor

`horus.com` **es un dominio público de Internet que pertenece a otra entidad**. Puedes usarlo dentro del hotel, pero ten en cuenta que:

- en la red del hotel, `horus.com` llevará a **tu** servidor, y la web real de horus.com dejará de verse desde los puestos;
- si algún día un puesto usa otro DNS (datos móviles, VPN…), `horus.com` irá a la web real, no a la tuya.

**Alternativas recomendadas** (el script funciona igual con cualquiera; solo cambia `DOMINIO`):

| Opción | Ejemplo | Ventaja |
|---|---|---|
| Subdominio del dominio real del hotel | `intranet.hotelhorus.es` | Lo controláis vosotros; sin choques con nadie. **La mejor.** |
| Nombre reservado para redes privadas (RFC 8375) | `horus.home.arpa` | Nunca existirá en Internet. |

Si decides seguir con `horus.com`, no pasa nada técnico: todo lo de esta guía funciona.

---

## 1. Generar los certificados (en el servidor)

Necesitas `openssl` y `bash`:

- **Linux (Ubuntu/Debian):** ya vienen; si falta, `sudo apt install openssl`.
- **Windows Server o Windows:** instala **Git para Windows** y abre **Git Bash** (incluye `openssl`).

> **Sin permisos de administrador en los puestos:** la CA puede instalarse solo para el usuario (el `.bat` lo hace automáticamente si no eres administrador), y la opción B del paso 3 (entrar por la IP) no necesita permisos.

1. Copia esta carpeta al servidor.
2. Edita la parte **CONFIGURA AQUÍ** de `generar_certificados.sh`:
   - `DOMINIO` y `NOMBRES_EXTRA`: los nombres con los que se entrará (`horus.com`, `www.horus.com`…).
   - `IPS_SERVIDOR`: la IP fija del servidor (por ejemplo `192.168.1.10`), para que también funcione `https://192.168.1.10`.
   - `RED_PERMITIDA`: el rango de vuestra red. Por defecto `192.168.0.0/255.255.0.0` (todas las `192.168.x.x`). Si vuestra red es `10.x.x.x`, pon `10.0.0.0/255.0.0.0`; si es `172.16–31.x.x`, `172.16.0.0/255.240.0.0`.
3. Ejecuta:
   ```bash
   bash generar_certificados.sh
   ```
   Te pedirá una contraseña para el `.pfx` (solo hace falta si usas IIS; si no, déjala vacía).

Se crea la carpeta `salida/`:

| Carpeta | Contenido | ¿Se reparte? |
|---|---|---|
| `salida/ca/` | `HorusCA.key` (**clave secreta de la CA**) y `HorusCA.crt` | ❌ **Nunca.** Guarda `HorusCA.key` en un USB cifrado fuera del servidor. |
| `salida/servidor/` | `horus.com.key`, `horus.com.fullchain.crt`, `horus.com.pfx` | ❌ Solo para el servidor web. |
| `salida/para_los_puestos/` | `HorusCA.cer` (Windows), `HorusCA.crt` (resto), `HUELLA_SHA256.txt` | ✅ Esto es lo que se instala en los puestos. |

### Medida de seguridad incluida: restricción de nombres

La CA se crea con una **restricción de nombres**: solo puede firmar certificados para `horus.com`, sus subdominios y las IP de vuestra red. Aunque alguien robara `HorusCA.key`, **no podría hacerse pasar por Google, el banco ni ninguna otra web** en vuestros puestos. Está comprobado: un certificado de `google.com` firmado con esta CA se rechaza (`permitted subtree violation`).

---

## 2. Configurar el servidor web

Usa `horus.com.key` y `horus.com.fullchain.crt` (certificado + CA). Ejemplos:

**Nginx**
```nginx
server {
    listen 443 ssl;
    server_name horus.com www.horus.com;
    ssl_certificate     /etc/ssl/horus/horus.com.fullchain.crt;
    ssl_certificate_key /etc/ssl/horus/horus.com.key;
    ssl_protocols TLSv1.2 TLSv1.3;
    root /var/www/horus;
}
server {                       # redirige http:// a https://
    listen 80;
    server_name horus.com www.horus.com;
    return 301 https://$host$request_uri;
}
```

**Apache** (`a2enmod ssl` y luego, en el VirtualHost `*:443`):
```apache
SSLEngine on
SSLCertificateFile    /etc/ssl/horus/horus.com.fullchain.crt
SSLCertificateKeyFile /etc/ssl/horus/horus.com.key
```

**IIS (Windows Server)**
1. Administrador de IIS ▸ servidor ▸ **Certificados de servidor** ▸ **Importar…** ▸ `horus.com.pfx` y su contraseña.
2. Sitio web ▸ **Enlaces…** ▸ **Agregar** ▸ tipo `https`, puerto 443, nombre de host `horus.com`, certificado `horus.com`.

Protege la clave del servidor: en Linux, `chmod 600 horus.com.key` y propietario `root`.

---

## 3. Que `horus.com` lleve al servidor (DNS)

Los puestos tienen que saber que `horus.com` es la IP del servidor. Elige **una** opción:

| Opción | Necesitas | Cuándo |
|---|---|---|
| **A. Registro en el DNS del router o de la empresa** | Acceso al router / al servidor DNS | Lo ideal: se hace una vez y vale para todos |
| **B. Sin DNS: entrar por la IP** | Nada | Lo más rápido; la dirección es menos bonita |
| **C. Archivo `hosts` en cada puesto** | Ser administrador de cada puesto | Pocos puestos, o mientras TI no añade el registro |
| **D. Nombre `horus.local` (mDNS)** | Servidor Linux | Sin tocar los puestos ni el router |

### A. Con acceso al DNS
Añade un registro `A`: `horus.com → 192.168.1.10` (y `www.horus.com`). En routers suele llamarse «DNS local» o «Host estático»; en Windows Server, consola **DNS** ▸ nueva zona `horus.com` ▸ registro A; en Pi-hole, *Local DNS Records*.

### Sin acceso al router ni al DNS de la empresa

**B. Entrar por la IP: `https://192.168.1.10`**
El certificado ya incluye la IP del servidor (`IPS_SERVIDOR`), así que sale el candado sin avisos. No hay que tocar nada más que instalar la CA (paso 4). Puedes crear en los puestos un acceso directo o un marcador llamado «Intranet Horus» que apunte a esa dirección.

**C. Archivo `hosts` en cada puesto**
Cada equipo aprende por su cuenta que `horus.com` es el servidor.
- Windows: edita la IP en `anadir_hosts_windows.bat` y ejecútalo **como administrador** (vuelve a ejecutarlo y elige «Quitar» para deshacerlo).
- Linux / macOS: edita la IP en `anadir_hosts_linux.sh` y ejecuta `bash anadir_hosts_linux.sh` (o `… quitar`).
- A mano: añade `192.168.1.10  horus.com www.horus.com` a `C:\Windows\System32\drivers\etc\hosts` (Bloc de notas como administrador) o a `/etc/hosts`.
- En móviles no se puede editar `hosts`: que entren por la IP (opción B).

**D. Nombre `horus.local` anunciado por el propio servidor (mDNS)**
Igual que las impresoras de red, el servidor se anuncia solo y Windows 10/11, macOS, Linux e iPhone lo encuentran sin configurar nada.
1. **Antes de crear la CA**, pon `NOMBRES_EXTRA="www.horus.com horus.local"` en `generar_certificados.sh` (la CA solo podrá firmar los dominios que tenga configurados al crearla).
2. En el servidor Linux: `sudo hostnamectl set-hostname horus` y `sudo apt install avahi-daemon` (en Ubuntu suele venir ya).
3. Desde un puesto: `ping horus.local` y abre `https://horus.local`.

Limitaciones: algunos Android no resuelven `.local`, y redes con VLAN separadas o un aislamiento entre clientes en la wifi lo bloquean. Si falla, usa la opción B.

### Dos avisos importantes si no administras la red
- **IP fija:** todas estas opciones necesitan que el servidor tenga siempre la misma IP. Sin acceso al router no puedes reservarla; si pones una IP fija a mano en el servidor, elige una **fuera del rango que reparte el router (DHCP)** para que no la reciba otro equipo. Lo más seguro es pedir a TI una IP reservada.
- **Habla con el departamento de TI.** En una red de empresa, montar un servidor e instalar certificados raíz en los puestos suele requerir su permiso. Además, añadir un registro DNS les lleva cinco minutos y te ahorra configurar `hosts` en cada equipo. Esta carpeta (con este README) es justo lo que necesitan para revisarlo.

Comprueba desde un puesto: `ping horus.com` (o `horus.local`) debe responder la IP del servidor.

---|---|---|
| **DNS del router o servidor DNS interno** (recomendada) | Añade un registro `A`: `horus.com → 192.168.1.10` (y `www.horus.com`). En routers suele llamarse «DNS local», «Host estático» o «DNS rebinding/Local DNS». En Windows Server: consola **DNS** ▸ nueva zona `horus.com` ▸ registro A. En Pi-hole: *Local DNS Records*. | Muchos puestos; se configura una vez. |
| Archivo `hosts` en cada puesto | Añade la línea `192.168.1.10  horus.com www.horus.com`. Windows: `C:\Windows\System32\drivers\etc\hosts` (Bloc de notas como administrador). Linux/macOS: `/etc/hosts`. | Pocos puestos o pruebas. |

Comprueba desde un puesto: `ping horus.com` debe responder la IP del servidor.

---

## 4. Instalar la CA en los puestos

Reparte **solo** el contenido de `salida/para_los_puestos/`. Antes de instalar, comprueba que la **huella SHA-256** coincide con `HUELLA_SHA256.txt`: así sabes que nadie ha cambiado el archivo por el camino.

### Windows 10/11 (Chrome, Edge y Firefox)
- **Automático:** copia `HorusCA.cer` e `instalar_ca_windows.bat` a una carpeta del puesto ▸ clic derecho en el `.bat` ▸ **Ejecutar como administrador**.
- **A mano:** doble clic en `HorusCA.cer` ▸ **Instalar certificado** ▸ **Equipo local** ▸ «Colocar todos los certificados en el siguiente almacén» ▸ **Entidades de certificación raíz de confianza** ▸ Finalizar.
- **Muchos equipos en dominio (Active Directory):** una directiva de grupo (GPO) lo instala en todos: *Configuración del equipo ▸ Directivas ▸ Configuración de Windows ▸ Configuración de seguridad ▸ Directivas de clave pública ▸ Entidades de certificación raíz de confianza* ▸ **Importar** `HorusCA.cer`.

Chrome y Edge usan el almacén de Windows. Para **Firefox**, el `.bat` crea una política que le hace confiar en ese almacén (o en Firefox: `about:config` ▸ `security.enterprise_roots.enabled` = `true`).

### Linux (Ubuntu, Debian, Mint…)
```bash
bash instalar_ca_linux.sh      # con HorusCA.crt en la misma carpeta
```
Lo instala en el sistema y en Chrome/Chromium y Firefox del usuario que lo ejecuta (repítelo con cada usuario del puesto).

### macOS
```bash
sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain HorusCA.crt
```
O doble clic en `HorusCA.crt` ▸ llavero **Sistema** ▸ abre el certificado ▸ **Confiar** ▸ «Al utilizar este certificado: **Confiar siempre**».

### Android
Copia `HorusCA.crt` al móvil ▸ **Ajustes ▸ Seguridad ▸ Más ajustes de seguridad ▸ Cifrado y credenciales ▸ Instalar un certificado ▸ Certificado de CA** (el menú cambia algo según el fabricante). Chrome lo aceptará; algunas apps ignoran las CA instaladas por el usuario, pero el navegador no.

### iPhone / iPad
1. Envía `HorusCA.crt` al dispositivo (por correo o AirDrop) y ábrelo ▸ **Ajustes ▸ Perfil descargado ▸ Instalar**.
2. **Imprescindible:** **Ajustes ▸ General ▸ Información ▸ Ajustes de confianza de certificados** ▸ activa «Hotel Horus - CA interna».

---

## 5. Comprobar que funciona

- En un puesto: abre `https://horus.com` ▸ candado sin avisos. Pulsa el candado ▸ el certificado debe estar **emitido por «Hotel Horus - CA interna»**.
- Desde cualquier equipo con `openssl`:
  ```bash
  openssl s_client -connect horus.com:443 -servername horus.com -CAfile HorusCA.crt </dev/null | grep "Verify return code"
  # Debe decir: Verify return code: 0 (ok)
  ```

| Aviso del navegador | Causa probable | Solución |
|---|---|---|
| `NET::ERR_CERT_AUTHORITY_INVALID` / «Emisor desconocido» | La CA no está instalada en ese puesto o navegador | Paso 4 (en Firefox, revisa la política) y reinicia el navegador |
| `NET::ERR_CERT_COMMON_NAME_INVALID` | Entras con un nombre que no está en el certificado | Añádelo a `NOMBRES_EXTRA`/`IPS_SERVIDOR` y regenera |
| `ERR_NAME_NOT_RESOLVED` o abre otra web | DNS | Paso 3 |
| `ERR_CERT_DATE_INVALID` | Certificado caducado o reloj del puesto mal | Renueva (paso 6) o corrige la hora |
| El servidor no arranca | Ruta o permisos de la clave | Revisa las rutas del paso 2 |

---

## 6. Mantenimiento

- **Renovar el certificado del servidor** (dura 825 días; apúntalo en el calendario): ejecuta otra vez `bash generar_certificados.sh` y reinicia el servidor web. **La CA se reutiliza, así que no hay que tocar los puestos.**
- **Añadir un nombre o cambiar la IP:** edita la configuración, vuelve a ejecutar el script y reinicia el servidor web.
- **La CA caduca a los 10 años.** Para crear una nueva, borra `salida/ca/` y ejecuta el script; después reinstala la nueva CA en los puestos.
- **Si sospechas que `HorusCA.key` se ha filtrado:** crea una CA nueva, instálala en los puestos y **elimina la antigua** (Windows: `certmgr.msc` / `certlm.msc` ▸ Entidades de certificación raíz de confianza ▸ «Hotel Horus - CA interna» ▸ Eliminar). La restricción de nombres limita el daño, pero no lo elimina para `horus.com`.

## Reglas de oro

1. `HorusCA.key` **nunca** sale del servidor, salvo a su copia de seguridad cifrada. Nunca por correo, chat ni repositorio.
2. A los puestos solo va `HorusCA.cer` / `HorusCA.crt` (la parte pública).
3. Comprueba siempre la huella antes de instalar.
4. Usa esta CA solo para servicios del hotel. Nunca para inspeccionar el tráfico de los usuarios.
