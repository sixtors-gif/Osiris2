@echo off
rem ==========================================================================
rem  Instala la CA interna del Hotel Horus en este puesto Windows.
rem  Pon este archivo junto a HorusCA.cer y ejecutalo con
rem  clic derecho > "Ejecutar como administrador" (vale para todos los usuarios).
rem  Sin permisos de administrador se instala solo para el usuario actual.
rem ==========================================================================
setlocal
set "CA=%~dp0HorusCA.cer"
if not exist "%CA%" (echo No encuentro HorusCA.cer junto a este archivo. & pause & exit /b 1)

echo Huella SHA-256 del certificado que vas a instalar:
certutil -hashfile "%CA%" SHA256 | findstr /v ":"
echo Comprueba que coincide con la que te dio el administrador (HUELLA_SHA256.txt).
echo.
choice /m "Coincide y quieres instalarla"
if errorlevel 2 exit /b 1

net session >nul 2>&1
if %errorlevel%==0 (
  certutil -addstore -f Root "%CA%" >nul && echo [OK] Instalada para todos los usuarios del equipo.
) else (
  certutil -user -addstore -f Root "%CA%" >nul && echo [OK] Instalada solo para el usuario actual ^(no eres administrador^).
)

rem Firefox usa su propio almacen: le pedimos que confie en el de Windows,
rem solo si no hay ya una politica (para no pisar la configuracion existente).
set "FF=%ProgramFiles%\Mozilla Firefox"
if exist "%FF%\firefox.exe" (
  if not exist "%FF%\distribution\policies.json" (
    mkdir "%FF%\distribution" 2>nul
    > "%FF%\distribution\policies.json" echo {"policies":{"Certificates":{"ImportEnterpriseRoots":true}}}
    if exist "%FF%\distribution\policies.json" (echo [OK] Firefox confiara en la CA de Windows.) else (echo [!] Para Firefox, ejecuta como administrador.)
  ) else (
    echo [!] Firefox ya tiene policies.json: anade a mano "Certificates": {"ImportEnterpriseRoots": true}
  )
)
echo.
echo Cierra y vuelve a abrir el navegador y entra en https://horus.com
pause
