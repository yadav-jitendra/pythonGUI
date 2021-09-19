from tkinter import *

mainwindow = Tk()
mainwindow.geometry("200x200")

entry = Entry(mainwindow, width=30, borderwidth=2)
entry.insert(0, "Enter your name")
entry.pack()


def myClick():
    mylabel = Label(mainwindow, text="Hello " + entry.get())
    mylabel.pack()


myButton = Button(mainwindow, text="Click Me", command=myClick, fg="red", bg="blue")
myButton.pack()


mainwindow.mainloop()
