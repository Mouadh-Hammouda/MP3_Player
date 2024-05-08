
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
mixer.init()

frameCnt = 30
frames = [PhotoImage(file = "icons/galaxy.gif", format = 'gif -index %i' %(i))for i in range(frameCnt)]

def update(ind):
    frame = frames[ind]
    ind +=1 
    if ind == frameCnt: 
        ind = 0
    label.configure(image = frame)
    root.after(40, update, ind)


label = Label(root)
label.place(x = -15, y = -20)
root.after(0, update, 0)

def AddMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path) 
        songs = os.listdir(path)

    for song in songs:
        if song.endswith(".mp3"):
            Playlist.insert(END,song)

def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    #print(Music_Name(ACTIVE))
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()



app_icon = PhotoImage(file = "icons/mp3-datei.png")
root.iconphoto(False, app_icon)

Menu = PhotoImage(file = "icons/menu.png")
Label(root, image = Menu).place(x = 0,y = 580,width = 485, height = 100)

Frame_Music = Frame(root, bd = 2, relief = RIDGE)
Frame_Music.place(x = 0, y = 585, height = 100 )

lower_frame = Frame(root, bg = "#c9dfc9", width = 485, height= 100)
lower_frame.place(x = 0, y = 450)

ButtonPlay = PhotoImage(file = "icons/play.png")
ButtonStop = PhotoImage(file = "icons/stop.png")
ButtonPause = PhotoImage(file = "icons/pause.png")
Volume1 = PhotoImage(file = "icons/volume-up.png")
panel = Label(root, image = Volume1).place(x = 20, y = 487)

Button(root, image = ButtonPause, bg ="#c9dfc9", bd = 0, height = 60, width = 60, command = mixer.music.pause).place(x = 300, y = 487)
Button(root, image = ButtonStop, bg ="#c9dfc9", bd = 0, height = 60, width = 60, command = mixer.music.stop).place(x = 130, y = 487)
Button(root, image = ButtonPlay, bg = "#c9dfc9", bd = 0, height = 60, width = 60, command = PlayMusic).place(x = 215,  y = 487)
Button(root, text = "Browse Music",width = 59, height = 1, font = ("Comic Sans MS", 12, "bold"), fg = "Black", bg = "#FFFFFF", command = AddMusic).place(x = 0, y = 550)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width = 100, font = ("Comic Sans MS", 10), bg = "#333333", fg = "grey", selectbackground = "lightblue", cursor = "hand2",bd = 0, yscrollcommand  = Scroll.set)
Scroll.config(command = Playlist.yview)
Scroll.pack(side = RIGHT, fill = Y)
Playlist.pack(side = RIGHT, fill = BOTH)

root.mainloop()
