from tkinter import *

root = Tk()
root.title("Python GUI")

frame = LabelFrame(root, text="this is a frame", padx=50, pady=50)  # padding inside of a frame
frame.pack(padx=10, pady=10)    # padding outside of a frame

button = Button(frame, text="Click")
button2 = Button(frame, text="Click 2")
button.grid(row=0, column=0)
button2.grid(row=0, column=1)
# button.pack()                 # cannot use pack and grid generally, but with frame and other widget

root.mainloop()