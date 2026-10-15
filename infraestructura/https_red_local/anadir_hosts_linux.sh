#!/usr/bin/env bash
# Hace que este puesto Linux/macOS sepa que horus.com es el servidor del hotel
# (añade una línea a /etc/hosts). Uso: bash anadir_hosts_linux.sh   |   Quitar: bash anadir_hosts_linux.sh quitar
set -euo pipefail
IP="192.168.1.10"
NOMBRES="horus.com www.horus.com"
MARCA="# Servidor interno Hotel Horus"
sudo cp /etc/hosts /etc/hosts.copia_seguridad
sudo sed -i.tmp "/$MARCA/d" /etc/hosts && sudo rm -f /etc/hosts.tmp
if [[ "${1:-}" != "quitar" ]]; then
  printf '%s\t%s\t%s\n' "$IP" "$NOMBRES" "$MARCA" | sudo tee -a /etc/hosts >/dev/null
  echo "[OK] $NOMBRES → $IP"
else
  echo "[OK] Entrada quitada."
fi
