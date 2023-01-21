@ECHO off
@REM check if python installed
python --version | find /v "Python" >NUL 2>NUL && (ECHO please install python 3 first)
python --version | find "Python"    >NUL 2>NUL && (GOTO :INSTALL_PACKAGES)

:INSTALL_PACKAGES
pip install selenium
pip install bs4
pip install datetime
pip install random
pip install playsound==1.2.2 
pip install lxml
GOTO :RUN_APP

:RUN_APP
python app.py
