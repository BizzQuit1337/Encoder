@ECHO OFF
ECHO starting ...
CALL unlocker.bat
DIR
CALL encoder.py
CALL locker.bat
