import tkinter as tk
from tkinter import Label
from tkinter import Button
from tkinter import messagebox


root = tk.Tk()
root.title("TKINTER import")
root.geometry("500x500")
root.configure(bg="blue")

label = Label(root, text='randomowy napis')
label.pack()

def commandforbutton():
    msg=messagebox.showinfo("randomowe okienko", "randomowe okienko")

button = Button(root, text='randomowy przycisk', command = commandforbutton)
button.place(x=250,y=250)

root.mainloop()
