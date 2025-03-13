import tkinter as tk
from tkinter import ttk 

root = tk.Tk()
con_var = tk.IntVar

title = ttk.Label(text = "Rock,Paper\n  Scissors")
title.grid(row = 0, column = 1, padx = 5, pady = 5)

title = ttk.Label(text = "Choose one")
title.grid(row = 1, column = 1, padx = 5, pady = 5)

b_Rock = ttk.Button(root, text = "Rock")
b_Rock.grid(row = 2, column = 0)

b_Paper = ttk.Button(root, text = "Paper")
b_Paper.grid(row = 2, column = 1)

b_Scissor = ttk.Button(root, text = "Scissor")
b_Scissor.grid(row = 2, column = 2)

tittle = ttk.Label(text = "Score: 0")
tittle.grid(row = 3, column = 1)

tittle = ttk.Label(text = "Computer: 0")
tittle.grid(row = 4, column = 1)

root.mainloop()