from tkinter import *
from PIL import ImageTk, Image

mainwindow = Tk()
mainwindow.title("Image Viewer")

my_img1 = ImageTk.PhotoImage(Image.open("images/image1.jpg").resize((500, 500), Image.ANTIALIAS))
my_img2 = ImageTk.PhotoImage(Image.open("images/image2.jpg").resize((500, 500), Image.ANTIALIAS))
my_img3 = ImageTk.PhotoImage(Image.open("images/image3.jpg").resize((500, 500), Image.ANTIALIAS))

image_list = [my_img1, my_img2, my_img3]

my_label = Label(image=image_list[0])
my_label.grid(row=0, column=0, columnspan=3)

status_bar = Label(mainwindow, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)


def toggle_image(image_position):
    global my_label
    global button_forwd
    global button_back
    global status_bar

    my_label.grid_forget()
    my_label = Label(image=image_list[image_position])

    nextImg = (image_position + 1) % 3
    previous = (image_position - 1) % 3
    button_forwd = Button(mainwindow, text=">>", command=lambda: toggle_image(nextImg))
    button_back = Button(mainwindow, text="<<", command=lambda: toggle_image(previous))

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forwd.grid(row=1, column=2)

    status_bar = Label(mainwindow, text="Image " + str(image_position + 1) + " of " + str(len(image_list)), bd=1,
                       relief=SUNKEN, anchor=E)
    status_bar.grid(row=2, column=0, columnspan=3, sticky=W + E)


button_back = Button(mainwindow, text="<<", command=lambda: toggle_image(-1))
button_quit = Button(mainwindow, text="Exit", command=mainwindow.quit)
button_forwd = Button(mainwindow, text=">>", command=lambda: toggle_image(1))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forwd.grid(row=1, column=2, pady=10)

status_bar.grid(row=2, column=0, columnspan=3, sticky=W + E)

mainwindow.mainloop()
