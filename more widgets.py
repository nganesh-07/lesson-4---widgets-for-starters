from tkinter import *
from datetime import date

# create window
root = Tk()
root.title("Getting started with widgets")
root.geometry("400x300")

lbl = Label(text="Hey!", fg="white", bg="#072F5F", height=1, width=300)

# add another label for getting name as input from user
# use entry widget for textbox to enter name
name_lbl = Label(text="Full Name", bg="#3895d3")
name_entry = Entry()

# function to display message
def display():
    name = name_entry.get() # read input given by user
    global message
    message = "Welcome to the application! \nToday's date is: "
    greet = "Hello", name, "!"
# details of textbox
    textbox.insert(END, greet)
    textbox.insert(END, message)
    textbox.insert(END, date.today())

textbox = Text(height=3) # add textbox widget

btn = Button(text="Begin", command=display, height=1, bg="#1261A0", fg="white")

# organize widgets in window
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
textbox.pack()

root.mainloop()
