# Settings für QO-100 Programm

com_port = 'COM1'  # COM-Port für CAT, der verwendet werden soll.
baudrate = 9600  # Baudrate für CAT

# Pfad zur SDR-Console
sdr_console_path = '"C:\\Program Files\\SDR-Radio.com (V3)\\SDR Console.exe"'

qo100_cat = {
    # CAT-Befehl :  Beschreibung
    'FA432431000': 'Frequenz auf VFO-A 432,431MHz',
    'OS00': 'Simplexbetrieb',
    'CT00': 'CTCSS AUS',
    'MD02': 'MODE auf USB',
    'PC005': 'Sendeleistung auf 5W',
    'EX140010' : 'Maximale Sendeleistung auf 10W begrenzen',
    'LK1' : 'LOCK einschalten',
    'MG030' : 'MIC GAIN auf 30'
}

normal_cat = {
    # CAT-Befehl :  Beschreibung
    'MC003': 'Memory Channel 003',
    'PC010': 'Sendeleistung auf 10W',
    'EX140020' : 'Maximale Sendeleistung auf 20W begrenzen',
    'LK1' : 'LOCK einschalten',
    'MG070' : 'MIC GAIN auf 70'
}
