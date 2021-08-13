import os
from tkinter import *
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
    # normal_button.config(state=DISABLED)
    print(ser.name)
    ser.write(b'FA432431000;OS00;CT00;MD02;PC005;')
    ret = ser.readline()
    print(ret)
    label2.config(text="QO-100 Betrieb geschaltet!")
    # os.system('cat-qo100.cmd')
    # normal_button.config(state=ACTIVE)


# Prozedur für Normal Button
def normal():
    print(ser.name)
    ser.write(b'MC003;PC010;')
    ret = ser.readline()
    print(ret)
    # os.system('cat-normal.cmd')
    label2.config(text="NORMAL Betrieb geschaltet!")



# Copyright-Label
label1 = Label(root, text="QO-100 v" + __version__ + "\n\xa9 08/2021 by Erik Schauer, DO1FFE")
label1.pack()

# Button für Normal-Betrieb
normal_button = Button(root, text="Normal", command=normal)
normal_button.grid(row=0, coloumn=0, pady=10)

# Button für QO-100 Betrieb
qo100_button = Button(root, text="QO-100", command=qo100)
qo100_button.grid(row=0, coloumn=1, padx=10)

label2 = Label(root, text="Bitte Betriebsmodus wählen!")
label2.pack(pady=10)


root.mainloop()
ser.close()
