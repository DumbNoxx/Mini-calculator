#!/usr/bin/env python3 

import tkinter as tk
from tkinter import messagebox
import math
import os
from dotenv import load_dotenv

load_dotenv()
icon = os.getenv("ICON")
wallpaper_env = os.getenv('WALLPAPER')
screen = tk.Tk()
screen.geometry("600x350")
screen.title("Mini calculator")
icon_1 = tk.PhotoImage(file=icon)
wallpaper_1 = tk.PhotoImage(file=wallpaper_env)

wallpaper = tk.Label(screen,image=wallpaper_1)
wallpaper.place(x=0,y=0,relwidth=1,relheight=1)

label1 = tk.Label(screen,text='First number',bg='yellow')
label1.place(x=10,y=10,width=120,height=30)

text1 = tk.Entry(screen,bg='pink')
text1.place(x=150,y=10,width=120,height=30)

label2 = tk.Label(screen,text='Second number',bg='yellow')
label2.place(x=10,y=50,width=120,height=30)

text2 = tk.Entry(screen,bg='pink')
text2.place(x=150,y=50,width=120,height=30)

def addition():
	n1 = text1.get()
	n2 = text2.get()

	r = float(n1) + float(n2)
	text3.delete(0,'end')
	text3.insert(0,r)
	label = tk.Label(screen,text=f'You have added {n1} plus {2}')
	label.place(x=220,y=330)
	screen.after(600,label.destroy)

button1 = tk.Button(screen,text='Addition',command=addition)
button1.place(x=360,y=250,width=120,height=30)

def subtraction():
	n1 = text1.get()
	n2 = text2.get()

	r = float(n1) - float(n2)
	text3.delete(0,'end')
	text3.insert(0,r)
	label = tk.Label(screen,text=f'You have subtracted {n1} minus {2}')
	label.place(x=220,y=330)
	screen.after(600,label.destroy)

button2 = tk.Button(screen,text='Subtraction',command=subtraction)
button2.place(x=480,y=250,width=120,height=30)


def multiplication():
	n1 = text1.get()
	n2 = text2.get()

	r = float(n1) * float(n2)
	text3.delete(0,'end')
	text3.insert(0,r)
	label = tk.Label(screen,text=f'You have multiplied {n1} by {2}')
	label.place(x=220,y=330)
	screen.after(600,label.destroy)

button3 = tk.Button(screen,text='Multiplication',command=multiplication)
button3.place(x=360,y=290,width=120,height=30)

def division():
	n1 = text1.get()
	n2 = text2.get()

	r = float(n1) / float(n2)
	text3.delete(0,'end')
	text3.insert(0,r)
	label = tk.Label(screen,text=f'You have divided {n1} by {2}')
	label.place(x=220,y=330)
	screen.after(600,label.destroy)


button4 = tk.Button(screen,text='Division',command=division)
button4.place(x=480,y=290,width=120,height=30)


def power():
	n1 = text1.get()
	n2 = text2.get()

	r = pow(float(n1),float(n2))
	text3.delete(0,'end')
	text3.insert(0,r)
	label = tk.Label(screen,text=f'you have power of {n1} to {n2}')
	label.place(x=220,y=330)
	screen.after(600,label.destroy)

button5 = tk.Button(screen,text='Power of the number N',command=power)
button5.place(x=390,y=200,width=180,height=30)


def root():
	n1 = text1.get()
	n2 = text2.get()

	r = float(n1) ** (1/float(n2))
	text3.delete(0,'end')
	text3.insert(0,r)
	label = tk.Label(screen,text=f'You have obtained the root {n2} of {n1}')
	label.place(x=220,y=330)
	screen.after(600,label.destroy)

button6 = tk.Button(screen,text='Root N of a number',command=root)
button6.place(x=390,y=150,width=180,height=30)


label3 = tk.Label(screen,text='Result',bg='yellow')
label3.place(x=10,y=120,width=120,height=30)

text3 = tk.Entry(screen,bg='pink')
text3.place(x=150,y=120,width=120,height=30)


def leave():
    resultado = messagebox.askquestion("Exit", 'Do you really want to go out', icon='question', default='no')

    if resultado == 'yes':
        screen.quit()

button4 = tk.Button(screen,text="Leave",command=leave)
button4.place(x=10,y=290,width=120,height=30)


screen.iconphoto(True,icon_1)
screen.mainloop()