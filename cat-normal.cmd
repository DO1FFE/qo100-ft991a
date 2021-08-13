@ECHO OFF
call settings.cmd

REM TX Power 50W ; Memory-Channel 003 (DB0NA)
set CAT=MC003;PC010;
echo Sende Befehl "%CAT%" an %COMPORT%
echo| set /p="%CAT%"> %COMPORT%
