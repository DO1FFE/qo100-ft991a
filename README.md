Dieses Python-Programm besteht aus der Datei ``main.py`` und einer Konfigurationsdatei
``settings.ini``.

``main.py`` stellt eine grafische Oberfläche bereit, um ein Amateurfunkgerät über
CAT-Kommandos zu steuern. Die Parameter für COM-Port, Baudrate und den Pfad zur
SDR-Console sowie die CAT-Befehle für Normal- und QO-100-Betrieb werden 
über ``settings.ini`` eingelesen.

Passen Sie die Werte in ``settings.ini`` an Ihre Umgebung an. Die Datei ist in
Abschnitte unterteilt:

``[general]``
  - ``com_port``: Name des seriellen Ports
  - ``baudrate``: Baudrate für die CAT-Verbindung
  - ``sdr_console_path``: Aufruf der SDR-Console

``[qo100_cat]`` und ``[normal_cat]`` enthalten die jeweiligen CAT-Befehle, die in
der angegebenen Reihenfolge ausgeführt werden.
