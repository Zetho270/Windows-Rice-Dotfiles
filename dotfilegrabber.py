import tkinter as tk 
from tkinter import *
from tkinter import PhotoImage
import PIL
from PIL import Image, ImageTk
import subprocess
from subprocess import call
import os

bgicon = 'pictures/app_icon.ico'
breakeruper = 1 # used to compartmentalize the code, because im a neat freak :P
root = tk.Tk()
if breakeruper == 1:
    w = '1000'
    
    roottitle = root.title('YASB Dotfile Grabber')
    root.iconbitmap(bgicon)
    root.geometry(w+'x563')
    root.configure(bg='#2a2d35')
    b = '#2a2d35'
    f = '#cccccc'
    bgnew = '#000000'
    imgbg = 'pictures/keyboard.png'
   
    widthplace = int(w)/2

# window configuring :)

def yaml_clicked():
    os.system('powershell.exe pwd')
    os.system('powershell.exe ./filegrabber_configyaml.ps1')

def css_clicked():
    os.system('powershell.exe ./filegrabber_stylescss.ps1')



#bglabel = tk.Label(root, image=myimage)

if breakeruper == 1:
    canvas = tk.Canvas(root, width='1920', height='1080', bg=b, highlightthickness=0)
    canvas.place(x=0, y=0)
    img = PhotoImage(file=imgbg)
    canvas.create_image(1920,1080, image=img, anchor = tk.SE )
# canvas setup, creating the canvas and putting the background in :)

if breakeruper == 1:
    canvas.create_text(widthplace, 50, text='YASB Dotfile Grabber', fill=f, font=('Terminal', 40, 'bold'))

    btn = tk.Button(root, text='Grab config.yaml', font=('Terminal', 30, 'bold'), bg=b, fg=f, command=yaml_clicked)
    btn.pack(pady = 110)

    canvas.create_text(widthplace, 210, text='Grabs config.yaml from either C:/Users/[username]/Appdata/Local/Yasb', fill=f, font=('Terminal', 15, 'bold'))
    canvas.create_text(widthplace, 240, text='or C:/Users/[username]/.config/yasb', fill=f, font=('Terminal', 15, 'bold'))

    btn2 = tk.Button(root, text='Grab styles.css', font=('Terminal', 30, 'bold'), bg=b, fg=f, command=css_clicked)
    btn2.pack()

    canvas.create_text(widthplace, 390, text='Grabs styles.css from either C:/Users/[username]/Appdata/Local/Yasb', fill=f, font=('Terminal', 15, 'bold'))
    canvas.create_text(widthplace, 420, text='or C:/Users/[username]/.config/yasb', fill=f, font=('Terminal', 15, 'bold'))
# all text and buttons on screen

root.mainloop()