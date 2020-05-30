#from tkinter import *
#root =Tk()
#photo = PhotoImage(file="aloeGT.png")
#label =Label(root,image=photo)
#label.pack()
#
#root.mainloop()

from tkinter import *

# pip install pillow
from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        load = Image.open("baboon.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        
root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.geometry("800x600")
root.mainloop()