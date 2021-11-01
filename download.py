import tkinter as tk
from tkinter import *
import os

top = tk.Tk()
top.geometry("200x150") #window size

def retrieve():
    os.system('cls' if os.name == 'nt' else 'clear')
    speed = float(my_entry.get())
    size = float(my_entry2.get())
    timeleft = (size*1024 / speed)/60 #calcuating the estimated time
    timeleft1 = str(timeleft)
    print('it will take ' + timeleft1 + ' minutes')
    
frame = Frame(top)
frame.pack()
#entry widgets
my_entry = Entry(frame, width = 20)
my_entry.insert(0,'Input DL speed (MB/s)')
my_entry.pack(padx = 5, pady = 5)
my_entry2 = Entry(frame, width = 15)
my_entry2.insert(0,'Input DL size (GB)')
my_entry2.pack(padx = 5, pady = 5)

Button = Button(frame, text = "Submit", command = retrieve)
Button.pack(padx = 5, pady = 5)
top.mainloop()