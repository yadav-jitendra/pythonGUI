from tkinter import *
from PIL import ImageTk, Image

mainwindow = Tk()
mainwindow.title("Image")

my_img = ImageTk.PhotoImage(Image.open("images/image1.jpg").resize((500, 500), Image.ANTIALIAS))
my_label = Label(image=my_img)
my_label.pack()


button_quit = Button(mainwindow, text="Exit", command=mainwindow.quit)
button_quit.pack()

mainwindow.mainloop()
