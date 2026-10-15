#!/usr/bin/env bash
# Genera los certificados dentro de un contenedor desechable (no instala nada en tu equipo).
# Uso, desde esta carpeta:  bash generar_con_docker.sh
# El resultado queda en ./salida
set -euo pipefail
cd "$(dirname "$0")"
docker run --rm -it -v "$PWD":/certs -w /certs ubuntu:24.04 bash -c '
  apt-get -qq update && apt-get -qq install -y openssl >/dev/null &&
  SALIDA=/certs/salida bash <(tr -d "\r" < generar_certificados.sh) &&
  chown -R '"$(id -u):$(id -g)"' salida'
