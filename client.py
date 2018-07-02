from tkinter import *

# creating a blank window
root = Tk()

top = Frame(root)
top.pack()
bottom = Frame(root)
bottom.pack(side=BOTTOM)


button1 = Button(top, text="Button 1", fg="red")
button2 = Button(top, text="Button 2", fg="green")
button3 = Button(top, text="Button 3", fg="blue")
button4 = Button(bottom, text="Button 4", fg="yellow")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()

root.mainloop()
