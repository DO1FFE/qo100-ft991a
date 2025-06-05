import os
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
import serial
import settings

# Versionsnummer des Programms
__version__ = '0.1i'

# COM-Port definieren
ser = serial.Serial(settings.com_port, settings.baudrate, timeout=1)

# Versuchen, COM-Port zu öffnen
try:
    ser.open()
except serial.SerialException:
    try:
        ser.close()
        ser.open()
    except Exception as e:
        messagebox.showerror(
            "Fehler", f"Konnte COM-Port nicht öffnen: {str(e)}"
        )

# GUI erstellen
root = tk.Tk()
root.title("QO-100 v" + __version__)
root.resizable(width=False, height=False)


def execute_cat_commands(commands: dict):
    cmd_list = ''
    for command in commands:
        cmd_list += command + ';'
    try:
        ser.write(bytes(cmd_list.encode('ascii')))
    except Exception as e:
        messagebox.showerror(
            "Fehler", f"Konnte Befehl nicht senden: {str(e)}"
        )


# Prozedur für QO-100 Button
def qo100():
    execute_cat_commands(settings.qo100_cat)
    label2.config(text="QO-100 Betrieb geschaltet!")
    console_button.config(state=tk.ACTIVE)
    qo100_button.config(state=tk.DISABLED)
    normal_button.config(state=tk.ACTIVE)


# Prozedur für Normal Button
def normal():
    execute_cat_commands(settings.normal_cat)
    label2.config(text="NORMAL Betrieb geschaltet!")
    console_button.config(state=tk.DISABLED)
    normal_button.config(state=tk.DISABLED)
    qo100_button.config(state=tk.ACTIVE)


# Prozedur für Start der SDR-Console
def sdr_console():
    console_button.config(state=tk.DISABLED)
    normal_button.config(state=tk.DISABLED)
    qo100_button.config(state=tk.DISABLED)
    label2.config(text="SDR-Console geöffnet! - Bitte manuell schließen!")
    try:
        os.system(settings.sdr_console_path)
    except Exception as e:
        messagebox.showerror(
            "Fehler", f"Konnte SDR-Console nicht öffnen: {str(e)}"
        )
    console_button.config(state=tk.ACTIVE)
    qo100_button.config(state=tk.DISABLED)
    normal_button.config(state=tk.ACTIVE)


tabellenbreite = 3

# Copyright-Label
label1 = tk.Label(root, text="QO-100 Steuerung v" + __version__)
label1_2 = tk.Label(
    root,
    text="Software: © 08/2023 by DO1FFE\nHardware: © 08/2021 by DO7GJ",
)
myFont = font.Font(size=20)
label1['font'] = myFont
label1.grid(row=0, column=0, columnspan=tabellenbreite)
label1_2.grid(row=1, column=0, columnspan=tabellenbreite)

# Button für Normal-Betrieb
normal_button = tk.Button(
    root, text="Normal", pady=10, padx=50, command=normal
)
normal_button.config(state=tk.DISABLED)
normal_button.grid(row=2, column=0, pady=10, padx=10)

# Button für QO-100 Betrieb
qo100_button = tk.Button(root, text="QO-100", pady=10, padx=50, command=qo100)
qo100_button.config(state=tk.ACTIVE)
qo100_button.grid(row=2, column=1, padx=10)

# Button für SDR-Console starten
console_button = tk.Button(
    root, text="SDR-Console", pady=10, padx=50, command=sdr_console
)
console_button.config(state=tk.DISABLED)
console_button.grid(row=2, column=2, padx=10)

# Hinweistexte
label2 = tk.Label(root, text="Bitte Betriebsmodus wählen!")
label2.grid(row=3, column=0, columnspan=tabellenbreite, pady=10)

# Programmschleife
root.mainloop()

# COM-Port wieder schließen
try:
    ser.close()
except Exception as e:
    messagebox.showerror(
        "Fehler", f"Konnte COM-Port nicht schließen: {str(e)}"
    )
