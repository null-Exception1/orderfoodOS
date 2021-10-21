
import nlp
import os
import csv
import tkinter
from tkinter import *
import time
from utils import storeorder,chatbot
import random
from PIL import ImageTk,Image

greetings = ["Welcome to Royal Cheese Restaurant, I'm Max, How may I serve you?","Food is heaven just like Royal Cheese Restaurant! Any favorites?","Welcome to Royal Cheese Restaurant, What would you like to order today?"]
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
                                     font = ('courier', 15, 'bold'))
entry1.focus_force()
canvas.create_window(775,500,window=entry1)

bg1 = Image.open('utils/bg.jpg')
bg1 = bg1.resize((1550,1080))
bg = ImageTk.PhotoImage(bg1)
canvas.create_image(775, 400, image=bg)
button = Button(text="Submit", width=10, command=callback)
canvas.create_window(775,600,window=button)
text = canvas.create_text(775, 300, text=random.choice(greetings), fill="black", font=('courier', 20, 'bold'))
canvas.pack()
