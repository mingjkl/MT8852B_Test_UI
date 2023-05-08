@echo off

setlocal EnableDelayedExpansion

set PYTHON_INSTALLER=python-3.11.3-amd64.exe
set PYTHON_INSTALL_DIR=C:\Python38

echo Installing Python...
start /wait %~dp0%PYTHON_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1 TargetDir=!PYTHON_INSTALL_DIR!

if %errorlevel% neq 0 (
    echo Failed to install Python.
    pause
    exit /b %errorlevel%
)

echo Adding Python to the system PATH...
set PATH=%PYTHON_INSTALL_DIR%;%PYTHON_INSTALL_DIR%\Scripts;%PATH%

echo Python installation complete.

echo Installing pip...
cd pip-23.0.1
python setup.py install

if %errorlevel% neq 0 (
    echo Failed to install pip.
    pause
    exit /b %errorlevel%
)

echo pip installation complete.

echo Installing PySide6...
pip install -i https://mirrors.aliyun.com/pypi/simple/ pyside6
echo PySide6 installation complete.

echo Installing PyInstaller...
pip install -i https://mirrors.aliyun.com/pypi/simple/ pyinstaller
echo PyInstaller installation complete.

echo Installing PyVisa...
pip install -i https://mirrors.aliyun.com/pypi/simple/ pyvisa
echo PyVisa installation complete.

echo Installing PySerial...
pip install -i https://mirrors.aliyun.com/pypi/simple/ pyserial
echo PySerial installation complete.

echo Install complete.


pause

