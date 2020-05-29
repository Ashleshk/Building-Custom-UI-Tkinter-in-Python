
from tkinter import *
# STEPS TO BUILD
# !. organise the Layout
#    -> frames creation  -invisible container
#
#
root =Tk()                
# 1 INVISIBLE TOP FRAME
topFrame=Frame(root)
topFrame.pack()

# BOTTOM Frame
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

Button1 = Button(topFrame,text="Button 1",fg="red")
Button2 = Button(topFrame,text="Button 2",fg="blue")
Button3 = Button(topFrame,text="Button 3",fg="green")
Button4 = Button(bottomFrame,text="Button 4",fg="purple")

Button1.pack(side=LEFT)
Button2.pack(side=LEFT)
Button3.pack(side=LEFT)
Button4.pack(side=BOTTOM)

root.mainloop()   


#  PACK()     --->    stack widgets in stack fashion