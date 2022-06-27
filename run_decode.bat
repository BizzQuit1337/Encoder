@ECHO OFF
CALL unlocker.bat
DIR
CALL decoder.py
CALL locker.bat
TIMEOUT 5