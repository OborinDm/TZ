from tkinter import *


x = Tk()
from tkinter import messagebox

def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value) ==1:
        value = value[1:]
    calc.delete(0, END)
    calc.insert(0,value+str(digit))

def add_operation(operation):
    value = calc.get()
    if value[-1] in "+-*/":
        value = value[:-1]
    calc.delete(0, END)
    calc.insert(0, value+operation)

def calculate():
    value = calc.get()
    if value[-1] in "+-*/":
        value = value+value[:-1]
    calc.delete(0, END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo("Внимание", "Ошибка! Введите толька цифры!")
        calc.insert(0, 0)
    except (ZeroDivisionError):
        messagebox.showinfo("Внимание", "Ошибка! На ноль делить нельзя!")
        calc.insert(0, 0)


def clear():
    calc.delete(0, END)
    calc.insert(0,0)


x.title ("Calculator")
x.config (bg="black")
x.geometry("240x285+1000+200")
photo = PhotoImage(file= "i.png")
x.iconphoto(False,photo)

calc = Entry(x, justify="right", bg="black", fg="white", font=("Arial", 15), width=15)
calc.insert(0, "0")
calc.grid(row=0, column=0, columnspan=3, stick="we")

Button(text="1", bg = "#454545", fg="#fff", font=("Arial", 13), command=lambda : add_digit(1)).grid(row=3, column=0, stick="wens", padx=5, pady=5)
Button(text="2", bg = "#454545", fg="#fff", font=("Arial", 13), command=lambda : add_digit(2)).grid(row=3, column=1, stick="wens", padx=5, pady=5)
Button(text="3", bg = "#454545", fg="#fff", font=("Arial", 13), command=lambda : add_digit(3)).grid(row=3, column=2, stick="wens", padx=5, pady=5)
Button(text="4", bg = "#454545", fg="#fff", font=("Arial", 13), command=lambda : add_digit(4)).grid(row=2, column=0, stick="wens", padx=5, pady=5)
Button(text="5", bg = "#454545", fg="#fff", font=("Arial", 13), command=lambda : add_digit(5)).grid(row=2, column=1, stick="wens", padx=5, pady=5)
Button(text="6", bg = "#454545", fg="#fff", font=("Arial", 13), command=lambda : add_digit(6)).grid(row=2, column=2, stick="wens", padx=5, pady=5)
Button(text="7", bg = "#454545", fg="#fff", font=("Arial", 13), command=lambda : add_digit(7)).grid(row=1, column=0, stick="wens", padx=5, pady=5)
Button(text="8", bg = "#454545", fg="#fff", font=("Arial", 13), command=lambda : add_digit(8)).grid(row=1, column=1, stick="wens", padx=5, pady=5)
Button(text="9", bg = "#454545", fg="#fff", font=("Arial", 13), command=lambda : add_digit(9)).grid(row=1, column=2, stick="wens", padx=5, pady=5)
Button(text="0", bg = "#454545", fg="#fff", font=("Arial", 13), command=lambda : add_digit(0)).grid(row=4, column=0, stick="wens", padx=5, pady=5)


Button(text="+", bg = "#db8400", fg="#fff", font=("Arial", 13), command=lambda : add_operation("+")).grid(row=1, column=3, stick="wens", padx=5, pady=5)
Button(text="-", bg = "#db8400", fg="#fff", font=("Arial", 13), command=lambda : add_operation("-")).grid(row=2, column=3, stick="wens", padx=5, pady=5)
Button(text="/", bg = "#db8400", fg="#fff", font=("Arial", 13), command=lambda : add_operation("/")).grid(row=3, column=3, stick="wens", padx=5, pady=5)
Button(text="*", bg = "#db8400", fg="#fff", font=("Arial", 13), command=lambda : add_operation("*")).grid(row=4, column=3, stick="wens", padx=5, pady=5)
Button(text=".", bg = "#454545", fg="#fff", font=("Arial", 13), command=lambda : add_operation(".")).grid(row=4, column=1, stick="wens", padx=5, pady=5)

Button(text="=", bg = "#db8400", fg="#fff", font=("Arial", 13), command=calculate).grid(row=4, column=2, stick="wens", padx=5, pady=5)
Button(text="C", bg = "#a1a1a1", fg="black", font=("Arial", 13), command=clear).grid(row=0, column=3, stick="wens", padx=5, pady=5)


x.grid_columnconfigure(0, minsize=60)
x.grid_columnconfigure(1, minsize=60)
x.grid_columnconfigure(2, minsize=60)
x.grid_columnconfigure(3, minsize=60)

x.grid_rowconfigure(1, minsize=60)
x.grid_rowconfigure(2, minsize=60)
x.grid_rowconfigure(3, minsize=60)
x.grid_rowconfigure(4, minsize=60)

x.mainloop()
