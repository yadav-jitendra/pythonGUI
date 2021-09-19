from tkinter import *

root = Tk()
root.title("Simple Calculator")

entry = Entry(root, width=45, borderwidth=2)
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)


def button_click(number):
    former = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(former) + str(number))


def button_calculate(operator):
    former = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(former) + operator)


def button_eql():
    former = entry.get()
    summ = eval(former)
    entry.delete(0, END)
    entry.insert(0, str(former) + " = " + str(summ))


def button_clr():
    entry.delete(0, END)


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=40, pady=20, command=lambda: button_calculate("+"))
button_sub = Button(root, text="-", padx=40, pady=20, command=lambda: button_calculate("-"))
button_mul = Button(root, text="*", padx=40, pady=20, command=lambda: button_calculate("*"))
button_div = Button(root, text="/", padx=40, pady=20, command=lambda: button_calculate("/"))
button_mod = Button(root, text="mod", padx=40, pady=20, command=lambda: button_calculate("%"))
button_clr = Button(root, text="C", padx=40, pady=20, command=button_clr)
button_eql = Button(root, text="=", padx=40, pady=20, command=button_eql)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)

button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)
button_clr.grid(row=4, column=0)
button_eql.grid(row=4, column=2)
button_mod.grid(row=5, column=0, columnspan=4)

root.mainloop()
