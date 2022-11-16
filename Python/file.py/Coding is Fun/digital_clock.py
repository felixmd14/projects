import tkinter 
from tkinter import Label 
import time

master = tkinter.Tk()
master.title('DAP Digital Clock')

def get_current_time():
    # hour = time.strftime('%I')
    # mins =time.strftime('%M')
    # secs = time.strftime('%S')
    # am_pm = time.strftime('%p')
    # the_time = hour + ":" + mins + ":" + secs, am_pm
    the_time = time.strftime('%I:%M:%S %p')
    my_time.config(text=the_time)
    my_time.after(200, get_current_time)

my_time = Label(master, font='Arial 100 bold', bg='beige', fg='black')
my_time.pack()

get_current_time()
master.mainloop()