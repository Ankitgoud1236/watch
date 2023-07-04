from tkinter import *
from tkinter.ttk import *

 

from time import strftime
 

root = Tk()
root.title('Clock')
 

def time():
    string = strftime('%H:%M:%S %p')
    lable.config(text=string)
    lable.after(1000, time)
 
 

lable = Label(root, font=("ds-digital", 40, 'bold'),
            background='black',
            foreground='red')

lable.pack(anchor='center')
time()
 
mainloop()   