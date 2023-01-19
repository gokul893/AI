from tkinter import *
from PIL import Image,ImageTk,ImageSequence
import time
from pygame import mixer
mixer.init()

root = Tk()
root.geometry("1920x1080")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open("C:\\Users\\Gokul raj\\Firstproject\\Folder 3\\GUIgif.gif")
    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=0
    for img in ImageSequence.Iterator(img):
        img=img.resize((1920,1080))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.02)
    root.destroy()

play_gif()
root.mainloop()