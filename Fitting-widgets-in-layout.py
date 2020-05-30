from tkinter import *

root = Tk()
one = Label(root,text="One",bg ="red",fg="white")
one.pack()
two = Label(root,text="Two",bg ="green",fg="black")
two.pack(fill=X)
Three = Label(root,text="Three",bg ="blue",fg="white")
Three.pack(side=LEFT,fill=Y)

root.mainloop()