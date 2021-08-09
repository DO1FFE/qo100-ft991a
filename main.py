import os
from tkinter import *

__version__ = '0.1a'

root = Tk()
root.title("QO-100 v" + __version__)
root.geometry("300x100")
root.resizable(width=False, height=False)


def qo100():
    normal_button.config(state=DISABLED)
    os.system('cat-qo100.cmd')
    normal_button.config(state=ACTIVE)


def normal():
    os.system('cat-normal.cmd')


label1 = Label(root, text="QO-100 v" + __version__ + "\n\xa9 08/2021 by Erik Schauer, DO1FFE")
label1.pack()
normal_button = Button(root, text="Normal", command=normal)
normal_button.pack()
qo100_button = Button(root, text="QO-100", command=qo100)
qo100_button.pack()


root.mainloop()
