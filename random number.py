# 20.01.2019
from tkinter import *
from random import randint
 
def display_random_number():
    buttonText.set(str(randint(int(x.get()),int(y.get()))))
 
root = Tk()
root.title("")
root["bg"] = "blue"
root.geometry("250x100")

x = StringVar()
y = StringVar()
r_label = Label(text="random number:")
x_label = Label(text="min number:      ")
y_label = Label(text="max number:      ")
 
x_label.grid(row=0, column=0, sticky="w")
y_label.grid(row=1, column=0, sticky="w")
r_label.grid(row=2, column=0, sticky="w")
x_entry = Entry(textvariable=x)
y_entry = Entry(textvariable=y)
 
x_entry.grid(row=0,column=1, padx=5, pady=5)
y_entry.grid(row=1,column=1, padx=5, pady=5)
 
buttonText = StringVar()
btn = Button(textvariable=buttonText,
             background="white",     
             foreground="black",     
             padx="100",             
             pady="30",              
             font ="20",          
             command=display_random_number) 

btn.place(x=100, y=58, height=22, width=126)

root.mainloop()
