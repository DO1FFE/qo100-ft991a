Dieses Python-Programm besteht aus zwei Dateien: main.py und settings.py.

In main.py wird ein grafisches Benutzeroberflächen(GUI)-Programm erstellt, das die Einstellungen eines Amateurfunkgeräts über den Computer steuert. Das Programm verwendet die Tkinter-Bibliothek für die grafische Benutzeroberfläche und die Serial-Bibliothek, um die Kommunikation mit dem Funkgerät über einen COM-Port zu ermöglichen.

Die GUI enthält drei Hauptbuttons: "Normal", "QO-100" und "SDR-Console". Der "Normal"-Button setzt das Funkgerät auf normale Betriebsparameter zurück, während der "QO-100"-Button spezielle Einstellungen für den QO-100 Satelliten aktiviert. Der "SDR-Console"-Button startet die SDR-Console-Anwendung.

Die settings.py-Datei enthält die notwendigen Einstellungen und CAT-Befehle (Computer Aided Transceiver) für den Normal- und QO-100-Betrieb. Diese Befehle werden verwendet, um das Funkgerät über den COM-Port zu steuern.

Im Normalbetrieb wird der Speicherkanal 003 ausgewählt, die Sendeleistung auf 10W eingestellt, die maximale Sendeleistung auf 20W begrenzt, das Gerät gesperrt und der Mikrofonverstärkung auf 70 gesetzt. Im QO-100-Betrieb wird die Frequenz auf VFO-A 432,431 MHz eingestellt, Simplexbetrieb aktiviert, CTCSS ausgeschaltet, der Betriebsmodus auf USB eingestellt, die Sendeleistung auf 5W reduziert, die maximale Sendeleistung auf 10W begrenzt, das Gerät gesperrt und der Mikrofonverstärkung auf 30 gesetzt.

Die main.py-Datei ist hauptsächlich für das GUI und die Kommunikation mit dem Funkgerät verantwortlich, während die settings.py-Datei die Konfigurationsparameter und CAT-Befehle für verschiedene Betriebsmodi bereitstellt.
