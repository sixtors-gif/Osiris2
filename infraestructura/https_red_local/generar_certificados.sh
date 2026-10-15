#!/usr/bin/env bash
# ============================================================================
#  Certificados HTTPS para la red local del hotel
#  Crea (una sola vez) una autoridad de certificación (CA) privada y, con ella,
#  el certificado del servidor. Ejecútalo EN EL SERVIDOR (Linux, o Windows con
#  «Git Bash»): así las claves privadas nunca salen de la red del hotel.
#
#  Uso:   bash generar_certificados.sh
#  Renovar el certificado del servidor: vuelve a ejecutarlo (la CA se reutiliza).
# ============================================================================
set -euo pipefail

# ----------------------------- CONFIGURA AQUÍ -------------------------------
NOMBRE_CA="Hotel Horus - CA interna"         # Nombre que verán los usuarios
ORGANIZACION="Hotel Horus"
DOMINIO="horus.com"                          # Dominio principal del servidor
NOMBRES_EXTRA="www.horus.com"                # Otros nombres separados por espacios (p. ej. "www.horus.com horus.local")
IPS_SERVIDOR="192.168.1.10"                  # IP(s) del servidor en la LAN, o vacío
RED_PERMITIDA="192.168.0.0/255.255.0.0"      # Red local en la que la CA puede firmar IPs
DIAS_CA=3650                                 # 10 años
DIAS_SERVIDOR=825                            # Máximo que aceptan Apple y la mayoría de navegadores
CLAVE_PFX="${CLAVE_PFX:-}"                   # Contraseña del .pfx para IIS (se pregunta si está vacía)
# ----------------------------------------------------------------------------

DIR="${SALIDA:-$(cd "$(dirname "$0")" && pwd)/salida}"   # SALIDA permite elegir la carpeta (Docker)
CA_DIR="$DIR/ca"; SRV_DIR="$DIR/servidor"; CLI_DIR="$DIR/para_los_puestos"
mkdir -p "$CA_DIR" "$SRV_DIR" "$CLI_DIR"
chmod 700 "$CA_DIR"
command -v openssl >/dev/null || { echo "Falta openssl. En Ubuntu: sudo apt install openssl. En Windows usa Git Bash."; exit 1; }

# Evita que Git Bash (MSYS) convierta los «/C=ES/...» en rutas de Windows
export MSYS_NO_PATHCONV=1

# 1) Autoridad de certificación ------------------------------------------------
if [[ -f "$CA_DIR/HorusCA.key" ]]; then
  echo "• La CA ya existe: se reutiliza ($CA_DIR/HorusCA.crt)."
else
  echo "• Creando la autoridad de certificación «$NOMBRE_CA»…"
  # La CA solo podrá firmar los dominios configurados (y sus subdominios).
  # OJO: decide los nombres ANTES de crear la CA; añadir un dominio nuevo después
  # (por ejemplo horus.local) obliga a crear otra CA y reinstalarla en los puestos.
  RESTRICCION_DNS=""
  for d in $(echo "$DOMINIO $NOMBRES_EXTRA" | tr ' ' '\n' | sed 's/^www\.//' | sort -u); do
    RESTRICCION_DNS="${RESTRICCION_DNS:+$RESTRICCION_DNS,}permitted;DNS:$d,permitted;DNS:.$d"
  done
  cat > "$CA_DIR/ca.cnf" <<CNF
[req]
distinguished_name=dn
prompt=no
utf8=yes
string_mask=utf8only
[dn]
C=ES
O=$ORGANIZACION
CN=$NOMBRE_CA
[v3_ca]
basicConstraints=critical,CA:TRUE,pathlen:0
keyUsage=critical,keyCertSign,cRLSign
subjectKeyIdentifier=hash
authorityKeyIdentifier=keyid:always
# Restricción de nombres: esta CA SOLO puede firmar para el dominio del hotel y la
# red local. Aunque su clave se filtrara, no serviría para suplantar otras webs.
nameConstraints=critical,$RESTRICCION_DNS,permitted;IP:$RED_PERMITIDA
CNF
  openssl genrsa -out "$CA_DIR/HorusCA.key" 4096 2>/dev/null
  chmod 600 "$CA_DIR/HorusCA.key"
  openssl req -x509 -new -key "$CA_DIR/HorusCA.key" -sha256 -days "$DIAS_CA" \
    -config "$CA_DIR/ca.cnf" -extensions v3_ca -out "$CA_DIR/HorusCA.crt"
fi

# 2) Certificado del servidor ---------------------------------------------------
echo "• Creando el certificado del servidor para $DOMINIO…"
SAN="DNS:$DOMINIO"
for n in $NOMBRES_EXTRA; do SAN="$SAN,DNS:$n"; done
for ip in $IPS_SERVIDOR; do SAN="$SAN,IP:$ip"; done
cat > "$SRV_DIR/servidor.cnf" <<CNF
[req]
distinguished_name=dn
prompt=no
utf8=yes
string_mask=utf8only
[dn]
C=ES
O=$ORGANIZACION
CN=$DOMINIO
[v3_srv]
basicConstraints=critical,CA:FALSE
keyUsage=critical,digitalSignature,keyEncipherment
extendedKeyUsage=serverAuth
subjectAltName=$SAN
subjectKeyIdentifier=hash
authorityKeyIdentifier=keyid
CNF
openssl genrsa -out "$SRV_DIR/$DOMINIO.key" 2048 2>/dev/null
chmod 600 "$SRV_DIR/$DOMINIO.key"
openssl req -new -key "$SRV_DIR/$DOMINIO.key" -config "$SRV_DIR/servidor.cnf" -out "$SRV_DIR/$DOMINIO.csr"
openssl x509 -req -in "$SRV_DIR/$DOMINIO.csr" -CA "$CA_DIR/HorusCA.crt" -CAkey "$CA_DIR/HorusCA.key" \
  -CAcreateserial -CAserial "$CA_DIR/HorusCA.srl" -sha256 -days "$DIAS_SERVIDOR" \
  -extfile "$SRV_DIR/servidor.cnf" -extensions v3_srv -out "$SRV_DIR/$DOMINIO.crt" 2>/dev/null
cat "$SRV_DIR/$DOMINIO.crt" "$CA_DIR/HorusCA.crt" > "$SRV_DIR/$DOMINIO.fullchain.crt"

# .pfx para IIS / Windows Server
if [[ -z "$CLAVE_PFX" ]]; then
  read -r -s -p "Contraseña para el archivo .pfx (IIS); déjala vacía para no crearlo: " CLAVE_PFX || CLAVE_PFX=""; echo
fi
if [[ -n "$CLAVE_PFX" ]]; then
  openssl pkcs12 -export -inkey "$SRV_DIR/$DOMINIO.key" -in "$SRV_DIR/$DOMINIO.crt" -certfile "$CA_DIR/HorusCA.crt" \
    -name "$DOMINIO" -passout "pass:$CLAVE_PFX" -out "$SRV_DIR/$DOMINIO.pfx"
fi

# 3) Lo que se reparte a los puestos (solo la parte PÚBLICA de la CA) ---------
cp "$CA_DIR/HorusCA.crt" "$CLI_DIR/HorusCA.crt"                       # Linux, macOS, Android, iOS
openssl x509 -in "$CA_DIR/HorusCA.crt" -outform DER -out "$CLI_DIR/HorusCA.cer"   # Windows (doble clic)

# 4) Comprobaciones -------------------------------------------------------------
openssl verify -CAfile "$CA_DIR/HorusCA.crt" "$SRV_DIR/$DOMINIO.crt" >/dev/null
HUELLA=$(openssl x509 -in "$CA_DIR/HorusCA.crt" -noout -fingerprint -sha256 | cut -d= -f2)
{ echo "Huella SHA-256 de «$NOMBRE_CA»"
  echo "Formato con dos puntos (Linux, macOS, navegadores): $HUELLA"
  echo "Formato de Windows (certutil):                     $(echo "$HUELLA" | tr -d ':' | tr 'A-F' 'a-f')"; } > "$CLI_DIR/HUELLA_SHA256.txt"
echo
echo "✔ Listo."
echo "  Servidor (NO repartir):  $SRV_DIR/$DOMINIO.key  +  $DOMINIO.fullchain.crt  (o $DOMINIO.pfx)"
echo "  Puestos (repartir):      $CLI_DIR/HorusCA.cer (Windows)  ·  HorusCA.crt (resto)"
echo "  Nombres incluidos:       $SAN"
echo "  Caduca el servidor:      $(openssl x509 -in "$SRV_DIR/$DOMINIO.crt" -noout -enddate | cut -d= -f2)"
echo "  Huella SHA-256 de la CA: $HUELLA"
echo
echo "⚠ Guarda $CA_DIR/HorusCA.key en un lugar seguro y sin conexión (USB cifrado)."
echo "  Quien tenga esa clave puede emitir certificados que tus puestos aceptarán."
