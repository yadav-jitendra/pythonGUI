from tkinter import *

mainwindow = Tk()
mainwindow.geometry("200x200")


def myClick():
    mylabel = Label(mainwindow, text="You clicked a button")
    mylabel.pack()


myButton = Button(mainwindow, text="Click Me", command=myClick, fg="red", bg="blue")
myButton.pack()


# myButton = Button(mainwindow, text="Click Me", padx=50, pady=50)
# myButton2 = Button(mainwindow, text="Click Me(Disabled)", state=DISABLED)
# myButton2.pack()

mainwindow.mainloop()
