from tkinter import *
import pyttsx3

master_window = Tk()
master_window.geometry('500x500')
master_window.title('Text to Speech')
master_window.configure(bg = 'beige')
my_app_name = Label(master_window, text = 'Text to Speech App',bg='beige', font='Helvitica 20 bold').pack()
my_app_name = Label(master_window,bg = 'beige', font = 'Helvitica 20 bold').pack()

msg = StringVar()
my_text = Entry(master_window, textvariable = msg, border = 10, width = 200).pack()

def play():
    text_to_speech = pyttsx3.init()
    my_text = msg.get()
    text_to_speech.say(my_text)
    text_to_speech.runAndWait()

def reset():
    msg.set('')

def close():
    master_window.destroy()

play_btn = Button(master_window, text='Play', font=18, command=play).place(x=150, y=200)
reset_btn = Button(master_window, text='Reset', font=18, command=reset).place(x=210, y=200)
close_btn = Button(master_window, text='Close',font=18, bg='red', command=close).place(x=300, y=200)
master_window.mainloop()