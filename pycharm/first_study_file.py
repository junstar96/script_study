from __future__ import print_function
from tkinter import *
from tkinter import font
import tkinter.messagebox

window = Tk()
def print_e(name):
    print(name)

def pros():
    dollar = float(e1.get())
    e2.insert(0, str(dollar*1200))


l1 = Label(window, text = "hello")
l2 = Label(window, text = "world")
l1.grid(row = 0, column = 0)
l2.grid(row = 1, column = 0)


e1 = Entry(window)
e2 = Entry(window)
e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)



button = Button(window, text="클릭!", command=pros) #이러면 주석이

button.grid(row = 2, column = 0)

window.mainloop()