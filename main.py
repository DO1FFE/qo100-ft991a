import os
from tkinter import *
import tkinter.font as font
import serial

__version__ = '0.1c'
ser = serial.Serial('COM1', 9600, timeout=1)

try:
    ser.open()
except:
    ser.close()
    ser.open()

root = Tk()
root.title("QO-100 v" + __version__)
root.geometry("300x150")
root.resizable(width=False, height=False)


# Prozedur für QO-100 Button
def qo100():
    # print(ser.name)
    ser.write(b'FA432431000;OS00;CT00;MD02;PC005;')
    # ret = ser.readline()
    # print(ret)
    label2.config(text="QO-100 Betrieb geschaltet!")
    console_button.config(state=ACTIVE)
    qo100_button.config(state=DISABLED)
    normal_button.config(state=ACTIVE)


# Prozedur für Normal Button
def normal():
    # print(ser.name)
    ser.write(b'MC003;PC010;')
    # ret = ser.readline()
    # print(ret)
    label2.config(text="NORMAL Betrieb geschaltet!")
    console_button.config(state=DISABLED)
    normal_button.config(state=DISABLED)
    qo100_button.config(state=ACTIVE)


def sdr_console():
    os.system('"C:\Program Files\SDR-Radio.com (V3)\SDR Console.exe"')
    label2.config(text="SDR-Console geöffnet!")
    console_button.config(state=ACTIVE)
    qo100_button.config(state=DISABLED)
    normal_button.config(state=ACTIVE)


tabellenbreite = 2

# Copyright-Label
label1 = Label(root, text="QO-100 v" + __version__ + "\n\xa9 08/2021 by DO1FFE")
myFont = font.Font(size=20)
label1['font'] = myFont
label1.grid(row=0, column=0, columnspan=tabellenbreite)


# Button für Normal-Betrieb
normal_button = Button(root, text="Normal", command=normal)
normal_button.config(state=DISABLED)
normal_button.grid(row=1, column=0, pady=10)


# Button für QO-100 Betrieb
qo100_button = Button(root, text="QO-100", command=qo100)
qo100_button.config(state=ACTIVE)
qo100_button.grid(row=1, column=1, padx=10)


# Button für SDR-Console starten
console_button = Button(root, text="SDR-Console", command=sdr_console)
console_button.config(state=DISABLED)
# console_button.grid(row=1, column=2, padx=10)


label2 = Label(root, text="Bitte Betriebsmodus wählen!")
label2.grid(row=2, column=0, columnspan=tabellenbreite, pady=10)

root.mainloop()
ser.close()
