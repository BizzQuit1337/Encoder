@ECHO OFF
ECHO unlocking
CACLS key.txt /P EVERYONE:F
ECHO unlocked