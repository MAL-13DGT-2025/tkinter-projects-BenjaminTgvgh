import tkinter as tk # MUST HAVE
from tkinter import ttk

def press(button):
    current = equation.set(equation.get() + button)
        
    symbols = ["+", "-", "*", "/"]
    
    if current[-1] in symbols:
        current.rstrip("+-*/")
    equation.set(current)

def clear():
    equation.set("")

def calculate():
    try:
        result = eval(equation.get())
        equation.set(result)
    except:
        equation.set("ERROR")

root = tk.Tk() # MUST HAVE

root.title("Calculator")
equation = tk.StringVar()


calc = ttk.Entry(root, textvariable = equation)
calc.grid(row = 0, column = 0, columnspan = 4)

b_7 = ttk.Button(root, text = "7", command = lambda:press("7"))
b_7.grid(row = 1, column = 0)

b_8 = ttk.Button(root, text = "8", command = lambda:press("8"))
b_8.grid(row = 1, column = 1)

b_9 = ttk.Button(root, text = "9", command = lambda:press("9"))
b_9.grid(row = 1, column = 2)

b_divide = ttk.Button(root, text = "/", command = lambda:press("/"))
b_divide.grid(row = 1, column = 3)

b_4 = ttk.Button(root, text = "4", command = lambda:press("4"))
b_4.grid(row = 2, column = 0)

b_5 = ttk.Button(root, text = "5", command = lambda:press("5"))
b_5.grid(row = 2, column = 1)

b_6 = ttk.Button(root, text = "6", command = lambda:press("6"))
b_6.grid(row = 2, column = 2)

b_multiply = ttk.Button(root, text = "*", command = lambda:press("*"))
b_multiply.grid(row = 2, column = 3)

b_1 = ttk.Button(root, text = "1", command = lambda:press("1"))
b_1.grid(row = 3, column = 0)

b_2 = ttk.Button(root, text = "2", command = lambda:press("2"))
b_2.grid(row = 3, column = 1)

b_3 = ttk.Button(root, text = "3", command = lambda:press("3"))
b_3.grid(row = 3, column = 2)

b_subtract = ttk.Button(root, text = "-", command = lambda:press("-"))
b_subtract.grid(row = 3, column = 3)

b_clear = ttk.Button(root, text = "CLR", command = clear)
b_clear.grid(row = 4, column = 0)


b_0 = ttk.Button(root, text = "0", command = lambda:press("0"))
b_0.grid(row = 4, column = 1)

b_equal = ttk.Button(root, text = "=", command = calculate)
b_equal.grid(row = 4, column = 2)

b_add = ttk.Button(root, text = "+", command = lambda:press("+"))
b_add.grid(row = 4, column = 3)


root.mainloop() # MUST HAVE