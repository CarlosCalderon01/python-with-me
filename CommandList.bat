@echo off
echo Seleccione el comando que desea ejecutar:
echo 1. Delete IMG Repeat
echo 2. Change Format IMG to (GIF, JPEG)
echo 3. Change All Name Use Count
echo 4. Change All Name Start one
echo 5. Testing


set /p opcion="Ingrese el número del comando: "

if "%opcion%"=="1" (
    python src\Manager\DeleteRepeat.py
) else if "%opcion%"=="2" (
    python src\Manager\ChangeAllFormatIMG.py
) else if "%opcion%"=="3" (
    python src\Manager\ChangeAllNameAll.py
) else if "%opcion%"=="4" (
    python src\Manager\ChangeAllNameOne.py
) else if "%opcion%"=="5" (
    python Temp\Testing.py
) else (
    echo Comando no reconocido
)

