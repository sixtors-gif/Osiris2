@echo off
rem Genera los certificados con Docker Desktop (Windows). Doble clic, o desde esta carpeta:
rem   generar_con_docker.bat
rem El resultado queda en la carpeta "salida".
cd /d "%~dp0"
docker run --rm -it -v "%cd%:/certs" -w /certs ubuntu:24.04 bash -c "apt-get -qq update && apt-get -qq install -y openssl >/dev/null && SALIDA=/certs/salida bash <(tr -d '\r' < generar_certificados.sh)"
pause
