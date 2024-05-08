
import time 
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os 


root = Tk()
root.title("MP3-Player")
root.geometry("485x700+290+10")
root.configure(background = "#909c86")
root.resizable(False, False)


lower_frame = Frame(root, bg = "#c9dfc9", width = 485, height= 180)
lower_frame.place(x = 0, y = 400)

app_icon = PhotoImage(file = "icons/mp3-datei.png")
root.iconphoto(False, app_icon)

#print("current working directory", os.getcwd())

root.mainloop()
