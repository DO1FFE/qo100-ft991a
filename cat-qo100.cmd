@ECHO OFF
call settings.cmd

REM TX Power 50W ; Memory-Channel 003 (DB0NA)
set CAT=FA433600000;OS00;CT00;MD02;PC010;
echo Sende Befehl "%CAT%" an %COMPORT%
echo| set /p="%CAT%"> %COMPORT%
REM "C:\Program Files\SDR-Radio.com (V3)\SDR Console.exe"
