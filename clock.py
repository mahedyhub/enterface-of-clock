import tkinter as ui
import time
from tkinter import PhotoImage, Label, Button
import datetime
import pygame





window = ui.Tk()
window.geometry('600x500')

def update_clock():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_or_pm = time.strftime("%p")
    time_text = hours + ":" + minutes + ":" + seconds + " " + am_or_pm
    digital_clock_lbl.config(text=time_text)
    digital_clock_lbl.after(1000, update_clock)


#Clock icon
img=PhotoImage(file='C:\\Users\\lenovo\\Desktop\\python image\\clock icon.png')
window.iconphoto(False,img)



window.title("time clock")

digital_clock_lbl = ui.Label(window, text="00:00:00",
                             font="Helvatica 72 bold")
digital_clock_lbl.pack()

update_clock()

window.mainloop()

update_clock()
