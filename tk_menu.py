import mysql.connector
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser as Color
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


mydb = mysql.connector.connect(
  host="localhost",
  user="sysbot",
  password="abcABC123",
  database="sismo_cl"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT mag_sis from sismos")

myresult = mycursor.fetchall()

""" for x in myresult:
  print(x) """

mag_list=[]
columnas = [item[0] for item in mycursor.fetchall()]
mag_list.append(myresult)
print(mag_list)


w = Tk()
w.wm_title("Embedding in Tk")
#w.config(bg="#%02x%02x%02x" % (250,190,0))

fig, ejes = Figure(figsize=(5, 4), dpi=100)
c = mag_list
ejes.plot(mag_list, label="Magnitudes")
""" t = np.arange(0, 3, .01) """
""" fig.add_subplot(111).scatter(t, 2 * np.sin(2 * np.pi * t)) """
fig.add_subplot(111).scatter(c, ejes)

canvas = FigureCanvasTkAgg(fig, master=w)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, w)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    w.quit()     # stops mainloop
    w.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = tkinter.Button(master=w, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)


# creamos el menú
menubar = Menu(w)
# configuramos el menú a la ventana principal
w.config(menu=menubar)

# Submenus que implementara nuestro menú
filemenu = Menu(menubar, tearoff=0)
editmenu = Menu(menubar)
helpmenu = Menu(menubar)
# Ahora los agregamos a la barra de menú
menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='Edit', menu=editmenu)
menubar.add_cascade(label='Help', menu=helpmenu)
# Ahora añadimos las acciones para cada submenu

def get_file():
    file = filedialog.askopenfilename(title='Choose file')
    print(file)

# File (New, Open, Save, Close, Exit)
filemenu.add_command(label='New')
filemenu.add_command(label='Open', command=get_file)
filemenu.add_command(label='Save')
filemenu.add_command(label='Close')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=w.quit)

def changue_color():
    color = Color.askcolor(title='Choose color')
    print(color)
    print(color[0])
    print(color[1])
    w.config(bg=f'{color[1]}')
    #w.config(bg="#%02x%02x%02x"%color[0])


# Edit
editmenu.add_command(label='Preferences', command=changue_color)
editmenu.add_command(label='Copy', command=None)

def help_message():
    messagebox.showinfo('About', 'Created by PSYCHO')
# Help (about)
helpmenu.add_command(label='About', command=help_message)


w.mainloop()