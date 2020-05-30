from tkinter import *
import tkinter.messagebox   


root=Tk()

tkinter.messagebox.showinfo('Window ttile','Monkeys can live for 100 years')
 
answer=tkinter.messagebox.askquestion('Question 1:',' do u like silly faces')
 
if answer == 'yes':
    print("B---D-")



root.mainloop()