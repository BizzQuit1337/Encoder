@ECHO OFF
ECHO locking
CACLS key.txt /P EVERYONE:N
ECHO locked