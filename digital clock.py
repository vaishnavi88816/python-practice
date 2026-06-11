from tkinter import *
from time import strftime

# window create
root = Tk()
root.title("Digital Clock")

# clock update function
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

# label design
label = Label(root, font=('Arial', 50, 'bold'),
              background='black',
              foreground='cyan')

label.pack(anchor='center')

time()

root.mainloop()