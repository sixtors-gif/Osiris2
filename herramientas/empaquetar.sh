#!/bin/sh
# Genera un ZIP SCORM por cada curso de cursos/ en paquetes/ (imsmanifest.xml en la raíz del ZIP).
set -e
cd "$(dirname "$0")/.."
mkdir -p paquetes
for d in cursos/*/; do
  n=$(basename "$d")
  rm -f "paquetes/$n.zip"
  (cd "$d" && zip -qrX "../../paquetes/$n.zip" .)
  echo "paquetes/$n.zip"
done
