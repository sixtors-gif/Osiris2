@echo off
rem Actualiza F:\Temas con la ultima version de los cursos del repositorio Osiris2.
rem Uso: doble clic en este archivo (requiere Git para Windows instalado).
rem Estructura resultante:
rem   F:\Temas\<curso>.zip                 paquete SCORM listo para Moodle
rem   F:\Temas\extracted\<curso>\...       el mismo curso descomprimido
rem Añade y sobrescribe archivos; no borra nada de lo que ya haya en F:\Temas.
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

if not exist "%DESTINO%\extracted" mkdir "%DESTINO%\extracted"

rem Paquetes ZIP directamente en F:\Temas
copy /Y "%REPO%\paquetes\*.zip" "%DESTINO%\" >nul

rem Cursos descomprimidos en F:\Temas\extracted\<curso>
for /D %%C in ("%REPO%\cursos\*") do (
  echo   %%~nxC
  robocopy "%%C" "%DESTINO%\extracted\%%~nxC" /E /NFL /NDL /NJH /NJS /NP >nul
)

echo.
echo F:\Temas actualizado.
pause
