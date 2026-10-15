#!/usr/bin/env bash
# Instala la CA interna del Hotel Horus en un puesto Linux (Ubuntu, Debian, Mint…).
# Uso: pon este script junto a HorusCA.crt y ejecuta:  bash instalar_ca_linux.sh
set -euo pipefail
CA="$(cd "$(dirname "$0")" && pwd)/HorusCA.crt"
NOMBRE="Hotel Horus - CA interna"
[[ -f "$CA" ]] || { echo "No encuentro HorusCA.crt junto al script."; exit 1; }

echo "Huella SHA-256: $(openssl x509 -in "$CA" -noout -fingerprint -sha256 | cut -d= -f2)"
read -r -p "¿Coincide con la que te dio el administrador? [s/N] " r; [[ "$r" =~ ^[sS]$ ]] || exit 1

# 1) Almacén del sistema (curl, apt, la mayoría de programas)
sudo install -m 644 "$CA" /usr/local/share/ca-certificates/HorusCA.crt
sudo update-ca-certificates >/dev/null && echo "[OK] Sistema"

# 2) Chrome/Chromium y Firefox usan su propia base de datos (NSS), por usuario
if ! command -v certutil >/dev/null; then sudo apt-get install -y libnss3-tools >/dev/null; fi
añadir(){ certutil -d "sql:$1" -D -n "$NOMBRE" 2>/dev/null || true; certutil -d "sql:$1" -A -t "C,," -n "$NOMBRE" -i "$CA" && echo "[OK] $2"; }
mkdir -p "$HOME/.pki/nssdb"; [[ -f "$HOME/.pki/nssdb/cert9.db" ]] || certutil -d "sql:$HOME/.pki/nssdb" -N --empty-password
añadir "$HOME/.pki/nssdb" "Chrome / Chromium"
for p in "$HOME"/.mozilla/firefox/*.default* "$HOME"/snap/firefox/common/.mozilla/firefox/*.default*; do
  [[ -f "$p/cert9.db" ]] && añadir "$p" "Firefox ($(basename "$p"))"
done
echo "Cierra y vuelve a abrir el navegador y entra en https://horus.com"
