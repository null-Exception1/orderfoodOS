import nlp
import os
import csv
import tkinter
from tkinter import *
import time
from utils import storeorder,chatbot
import random
from PIL import ImageTk,Image
from tkinter.ttk import *

greetings = ["Welcome to Royal Cheese Restaurant, I'm Max, How may I serve you?","Food is heaven just like Royal Cheese Restaurant! Any favorites?","Welcome to Royal Cheese Restaurant, What would you like to order today?"]
#---------------------------------------------------------Tkinter------------------------------------------------------
asking = False
info = True
text = None
wewinthese = False
def callback():
    #---------chatbot---------------
    global canvas
    global asking
    global info
    global text
    global wewinthese
    if info == True:
        ans = chatbot.get_answer(entry1.get())
        canvas.itemconfig(text, text=random.choice(greetings))
        info = False
        entry1.delete(0,END)
        entry1.insert(0,"")
        return None
    if asking == False:
        ans = chatbot.get_answer(entry1.get())
        if ans == None:
                tips = ["Did you try checking out the other window? There is a menu in that window","Did you try correctly naming your order?","Were you making small talk? Ah, I'm a bot.. so.."]
                canvas.itemconfig(text, text="We can't find that order in our menu. "+random.choice(tips))
        if ans[1] == 0:
            canvas.itemconfig(text, text="Do you want an order of "+ans[0][0]+" for $"+str(ans[0][1])+"?")
            asking = True
            entry1.delete(0,END)
            entry1.insert(0,"")
        elif ans[1] == 1:
            canvas.itemconfig(text, text=ans[0][0])
    elif asking == True:
        if "ye" in entry1.get().lower():
            canvas.itemconfig(text, text="Noted. Do you want anything else?")
        elif "no" in entry1.get().lower() or "nah" in entry1.get().lower():
            
        else:
            canvas.itemconfig(text, text="Oh okay. If i'm not able to get which order you want, you can try specifying it better.\nNext order please")
        asking = False
        entry1.delete(0,END)
        entry1.insert(0,"")
tk = tkinter.Tk()
tk.geometry("1920x1080")
tk.title('Chatbot')
canvas= Canvas(tk, width= 1920, height= 1080, bg="white")
input_text = ''
entry1 = tkinter.Entry(tk, textvariable = input_text, justify = CENTER,
                                     font = ('courier', 15, 'bold'),width = 40)
entry1.focus_force()
canvas.create_window(775,500,window=entry1)
style = Style()
 
style.configure('W.TButton', font =
               ('courier', 15, 'bold'),foreground='brown',background="brown")
menu = Toplevel(tk)
 

menu.title("Menu")


menu.geometry("471x667")


bg1 = Image.open('utils/bg.jpg')
bg = ImageTk.PhotoImage(bg1)

bg2 = Image.open('utils/CHEESE.png')
bg2 = bg2.resize((471, 667))
bg2 = ImageTk.PhotoImage(bg2)
canvas2= Canvas(menu, width= 471, height= 667, bg="white")

canvas2.create_image(235, 333, image=bg2)
canvas2.pack()
canvas.create_image(775, 450, image=bg)
button = Button(text="Submit", width=20, command=callback, style='W.TButton')
canvas.create_window(775,600,window=button)
text = canvas.create_text(775, 300, text="May I know your name and phone number before you order?", fill="black", font=('courier', 15, 'bold'))
canvas.pack()

