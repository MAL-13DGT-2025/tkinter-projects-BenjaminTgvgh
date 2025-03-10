import tkinter as tk
from tkinter import ttk 

root = tk.Tk()
con_var = tk.IntVar

title = ttk.Label(text = "Rock,Paper\n Scissors")
title.grid(row = 1, column = 1, columnspan = 2, padx = 10, pady = 10)

b_Rock = ttk.Button(root, text = "Rock")
b_Rock.grid(row = 0, column = 2)

root.mainloop()