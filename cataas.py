from cProfile import label
from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO

from pygame.examples.aliens import load_image

window = Tk()
window.title("Cats")
window.geometry("600x480")

label = Label()
label.pack()

url="https://cataas.com/cat"
img=load_image(url)

if img:
    label.config(image=img)
    label.image = img

window.mainloop()
