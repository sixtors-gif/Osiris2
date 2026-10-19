@echo off
rem ==========================================================================
rem  Hace que este puesto Windows sepa que horus.com es el servidor del hotel,
rem  sin tocar el router ni el DNS de la empresa (anade una linea al archivo hosts).
rem  Clic derecho > "Ejecutar como administrador".
rem  Para deshacerlo: ejecutalo de nuevo y elige "Quitar".
rem ==========================================================================
setlocal
rem ------------------------- CONFIGURA AQUI ---------------------------------
set "IP=10.210.232.155"
set "NOMBRES=horus.com www.horus.com horus.local"
rem --------------------------------------------------------------------------
set "HOSTS=%SystemRoot%\System32\drivers\etc\hosts"
set "MARCA=# Servidor interno Hotel Horus"

net session >nul 2>&1 || (echo Ejecutalo como administrador: clic derecho ^> "Ejecutar como administrador". & pause & exit /b 1)

choice /c AQ /m "A = Anadir %NOMBRES% -> %IP%   Q = Quitar"
if errorlevel 2 goto quitar

rem Quita una entrada anterior (por si ha cambiado la IP) y anade la nueva
findstr /v /c:"%MARCA%" "%HOSTS%" > "%TEMP%\hosts.nuevo"
>> "%TEMP%\hosts.nuevo" echo %IP%	%NOMBRES%	%MARCA%
copy /y "%HOSTS%" "%HOSTS%.copia_seguridad" >nul
copy /y "%TEMP%\hosts.nuevo" "%HOSTS%" >nul || (echo No se pudo escribir en hosts. Puede que lo bloquee el antivirus. & pause & exit /b 1)
ipconfig /flushdns >nul
echo [OK] %NOMBRES% apunta ahora a %IP%. Copia de seguridad: hosts.copia_seguridad
goto fin

:quitar
findstr /v /c:"%MARCA%" "%HOSTS%" > "%TEMP%\hosts.nuevo"
copy /y "%TEMP%\hosts.nuevo" "%HOSTS%" >nul
ipconfig /flushdns >nul
echo [OK] Entrada quitada.

:fin
del "%TEMP%\hosts.nuevo" 2>nul
echo Comprueba con:  ping horus.com
pause
