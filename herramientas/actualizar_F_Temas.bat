@echo off
rem Actualiza F:\Temas con la última versión de los cursos del repositorio Osiris2.
rem Uso: doble clic en este archivo (requiere Git para Windows instalado).
rem Copia cursos\ y paquetes\ a F:\Temas sin borrar nada de lo que ya haya allí.
setlocal
set "DESTINO=F:\Temas"
set "REPO=%~dp0.."
set "RAMA=claude/focused-franklin-3ugnxv"

echo Descargando la ultima version del repositorio...
git -C "%REPO%" pull origin %RAMA%
if errorlevel 1 (
  echo No se pudo actualizar el repositorio. Revisa la conexion o Git.
  pause
  exit /b 1
)

if not exist "%DESTINO%" mkdir "%DESTINO%"
robocopy "%REPO%\cursos"   "%DESTINO%\cursos"   /E /NFL /NDL /NJH /NP
robocopy "%REPO%\paquetes" "%DESTINO%\paquetes" /E /NFL /NDL /NJH /NP
copy /Y "%REPO%\README.md" "%DESTINO%\README.md" >nul

echo.
echo F:\Temas actualizado.
pause
