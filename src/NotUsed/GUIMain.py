from tkinter import *
top = Tk()
# Code to add widgets will go here...

bottomframe = Frame(top)
redbutton = Button(top, text="Define new action", fg="blue")
#text = Text(top)
#text.insert(INSERT, "hey")
#text.pack()
redbutton.pack( side = LEFT)



def helloCallBack():
   print("daa")

B = Button(top, text ="Hello", command = helloCallBack)

B.pack()



top.mainloop()