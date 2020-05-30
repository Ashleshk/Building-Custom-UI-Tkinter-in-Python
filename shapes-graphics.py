from tkinter import *

root =Tk()

canvas = Canvas(root,width=200,height=300)
canvas.pack()

blackLine =canvas.create_line(0,0,200,50)
redline =canvas.create_line(0,100,200,50,fill="red")

greenbox =canvas.create_rectangle(20,20,150,60,fill="green")


root.mainloop()