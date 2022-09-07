import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import PhotoImage
from tkinter import Label
from tkinter import Frame
from tkinter.messagebox import showinfo

from matplotlib.pyplot import cla



# create the root window
root = tk.Tk()
root.title('Data Improvement')
root.resizable(False, False)
root.geometry('720x720')


# Add image file
bg = PhotoImage(file = "GUI/background.png")

# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)

# Create Frame
frame1 = Frame(root)
frame1.pack(pady = 0 )

# add function
def selanjutnya():
     os.system('py GUI/data_improvement.py')

# open button
open_button = ttk.Button(
    root,
    text='buka data mentah',
    command=selanjutnya)
  
root.mainloop()