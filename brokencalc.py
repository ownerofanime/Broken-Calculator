# import tkinter
from tkinter import *

def hello_w():
    output_label.config(text="Hello World")

window = Tk()
window.title("broken calculator program")
window.geometry("600x600")

#ouput window
output_label = Label(window, text="", width = 18, height= 2, font=('arial', 30), bg="grey")
output_label.grid(row = 0, columnspan = 4, sticky='we')

#BUTTON FUNCTIONS
button = Button(window, text='+', height=4, width=9, font=('arial', 15), bg='grey', command=hello_w)
button.grid(row=1, column=3, sticky='we')

button = Button(window, text='-', height=4, width=9, font=('arial', 15), bg='grey', command=hello_w)
button.grid(row=2, column=3, sticky='we')

button = Button(window, text='*', height=4, width=9, font=('arial', 15), bg='grey', command=hello_w)
button.grid(row=3, column=3, sticky='we')

button = Button(window, text='/', height=4, width=9, font=('arial', 15), bg='grey', command=hello_w)
button.grid(row=4, column=1, sticky='we')

#NUMBER LINES
button = Button(window, text='1', height=4, width=9, font=('arial', 15), bg='grey', command=hello_w)
button.grid(row=1, column=0, sticky='we')
button = Button(window, text='2', height=4, width=9, font=('arial', 15), bg='grey', command=hello_w)
button.grid(row=1, column=1, sticky='we')
button = Button(window, text='3', height=4, width=9, font=('arial', 15), bg='grey', command=hello_w)
button.grid(row=1, column=2, sticky='we')
button = Button(window, text='4', height=4, width=9, font=('arial', 15), bg='grey', command=hello_w)
button.grid(row=2, column=0, sticky='we')
button = Button(window, text='5', height=4, width=9, font=('arial', 15), bg='grey', command=hello_w)
button.grid(row=2, column=1, sticky='we')
button = Button(window, text='6', height=4, width=9, font=('arial', 15), bg='grey', command=hello_w)
button.grid(row=2, column=2, sticky='we')
button = Button(window, text='7', height=4, width=9, font=('arial', 15), bg='grey', command=hello_w)
button.grid(row=3, column=0, sticky='we')
button = Button(window, text='8', height=4, width=9, font=('arial', 15), bg='grey', command=hello_w)
button.grid(row=3, column=1, sticky='we')
button = Button(window, text='9', height=4, width=9, font=('arial', 15), bg='grey', command=hello_w)
button.grid(row=3, column=2, sticky='we')
button = Button(window, text='0', height=4, width=9, font=('arial', 15), bg='grey', command=hello_w)
button.grid(row=4, column=0, sticky='we')

#clear button
button = Button(window, text='<', height=4, width=9, font=('arial', 15), bg='grey', command=hello_w)
button.grid(row=4, column=2, sticky='we')

#Equals button
button = Button(bg='grey', height=4, width=9, font=('arial', 15), text='=', command=hello_w)
button.grid(row=4, column=3, sticky='we')

window.mainloop()
