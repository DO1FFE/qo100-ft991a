import os
import tkinter.font as font
from tkinter import *
import serial
import smtplib
from email.message import EmailMessage
import time

__version__ = '0.1e'
ser = serial.Serial('COM1', 9600, timeout=1)


# Email Alerts
def email_alert(body):
    now = time.strftime("%d.%m.%Y %H:%M:%S - ", time.localtime(time.time()))
    body = str(now+body)
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = 'QO-100 Alert!'
    msg['to'] = 'do1ffe@darc.de'

    user = "es110178@gmail.com"
    password = "qeyfxdorutqxgolm!"

    msg['from'] = f"DL0HDB-Alert <{user}>"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()


email_alert("Das QO-100 Programm wurde gestartet...")

try:
    ser.open()
except:
    ser.close()
    ser.open()

root = Tk()
root.title("QO-100 v" + __version__)
# root.geometry("300x150")
root.resizable(width=False, height=False)


# Prozedur für QO-100 Button
def qo100():
    email_alert("Der QO-100 Button wurde benutzt...")
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
    email_alert("Der NORMAL Button wurde benutzt...")
    # print(ser.name)
    ser.write(b'MC003;PC010;')
    # ret = ser.readline()
    # print(ret)
    label2.config(text="NORMAL Betrieb geschaltet!")
    console_button.config(state=DISABLED)
    normal_button.config(state=DISABLED)
    qo100_button.config(state=ACTIVE)


def sdr_console():
    email_alert("Die SDR-Console wurde gestartet...")
    console_button.config(state=DISABLED)
    normal_button.config(state=DISABLED)
    qo100_button.config(state=DISABLED)
    label2.config(text="SDR-Console geöffnet! - Bitte manuell schließen!")
    os.system('"C:\Program Files\SDR-Radio.com (V3)\SDR Console.exe"')
    console_button.config(state=ACTIVE)
    qo100_button.config(state=DISABLED)
    normal_button.config(state=ACTIVE)


tabellenbreite = 3

# Copyright-Label
label1 = Label(root, text="QO-100 Steuerung v" + __version__)
label1_2 = Label(root, text="Software: \xa9 08/2021 by DO1FFE\nHardware: \xa9 08/2021 by DO7GJ")
myFont = font.Font(size=20)
label1['font'] = myFont
label1.grid(row=0, column=0, columnspan=tabellenbreite)
label1_2.grid(row=1, column=0, columnspan=tabellenbreite)

# Button für Normal-Betrieb
normal_button = Button(root, text="Normal", pady=10, padx=50, command=normal)
normal_button.config(state=DISABLED)
normal_button.grid(row=2, column=0, pady=10, padx=10)


# Button für QO-100 Betrieb
qo100_button = Button(root, text="QO-100", pady=10, padx=50, command=qo100)
qo100_button.config(state=ACTIVE)
qo100_button.grid(row=2, column=1, padx=10)


# Button für SDR-Console starten
console_button = Button(root, text="SDR-Console", pady=10, padx=50, command=sdr_console)
console_button.config(state=DISABLED)
console_button.grid(row=2, column=2, padx=10)


label2 = Label(root, text="Bitte Betriebsmodus wählen!")
label2.grid(row=3, column=0, columnspan=tabellenbreite, pady=10)

root.mainloop()
ser.close()
email_alert("Das QO-100 Programm wurde beendet...")