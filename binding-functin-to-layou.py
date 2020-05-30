from tkinter import *

root =Tk()

def printName(event):
    print("Chello my name is Ashlesh..")
    
button_1 = Button(root,text="Print my name")
button_1.bind("<Button-1>",printName)
button_1.pack()

root.mainloop()