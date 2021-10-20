import nlp
import os
import csv
import tkinter
from tkinter import *
import time
#---------------------------------------------------------Tkinter------------------------------------------------------
def callback():
    #---------chatbot---------------
    pass

tk = tkinter.Tk()
tk.geometry("1920x1080")
tk.title('Chatbot')
canvas= Canvas(tk, width= 1920, height= 1080, bg="white")
input_text = ''
entry1 = tkinter.Entry(tk, textvariable = input_text, justify = CENTER,
                                     font = ('courier', 25, 'bold'))
entry1.focus_force()
canvas.create_window(775,500,window=entry1)
text = canvas.create_text(775, 300, text="Hi, May i know your name and order?", fill="black", font=('courier', 50, 'bold'))

button = Button(text="Submit", width=10, command=callback)
canvas.create_window(775,600,window=button)
canvas.pack()


#---------------------------------------------------------NLP----------------------------------------------------------






#---------------------------------------------------------Extras-------------------------------------------------------
