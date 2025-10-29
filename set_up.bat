@echo off
echo ================================
echo   CONFIGURANDO ENTORNO PYTHON
echo ================================

:: Crear entorno virtual
python -m venv venv

:: Activar entorno virtual
call venv\Scripts\activate

:: Actualizar pip
pip install --upgrade pip

:: Instalar dependencias
pip install -r requirements.txt

echo ================================
echo   ENTORNO LISTO ✅
echo ================================
pause
