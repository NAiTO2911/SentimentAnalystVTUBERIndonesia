import tkinter as tk
import os
from tkinter import INSERT, ttk
from tkinter import filedialog as fd
from tkinter import PhotoImage
from tkinter import Label
from tkinter import Text
from tkinter.messagebox import showinfo

from matplotlib.pyplot import cla, text

# create the root window
root = tk.Tk()
root.title('Analisa Sentimen')
root.resizable(False, False)
root.geometry('300x150')


# Add image file
bg = PhotoImage(file = "GUI/background.png")

# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)

# 
def select_files():
    filetypes = (
        ('Datasheet files', '*.csv'),
        ('Text file', '*.txt'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected Files',
        message=filenames
    )
def selanjutnya():
     os.system('py GUI/data_improvement.py')
     
# open button
open_button = ttk.Button(
    root,
    text='buka data mentah',
    command=select_files
)

open_button.pack(expand=True)

open_button = ttk.Button(
    root,
    text='buka stop word',
    command=select_files
)

open_button.pack(expand=True)

open_button = ttk.Button(
    root,
    text='selanjutnya',
    command=selanjutnya
)

open_button.pack(expand=True)

root.mainloop()