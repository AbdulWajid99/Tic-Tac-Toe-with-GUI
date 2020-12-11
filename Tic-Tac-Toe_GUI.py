# import
import Tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar

# initialize
p1, p2 = 'Player_!', 'Player_2'
z = 0  # score of winner
sX, sO = 0, 0  # score of X and O
player = 'X'  # default icon

# Game GUI

root = tk.TK()
root.title("Tic-Tac-Toe")
root.resizable(0, 0)  # ?
