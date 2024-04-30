from tkinter import *
from tkinter import messagebox
import os

# FUNCTION OF DROP MASSAGE OF ERROR
def func():
    if var1.get() == "":
        messagebox.showwarning("Warning", "please enter your USERNAME...!")
    elif var2.get() == "":
        messagebox.showwarning("Warning", "please enter your PASSWORD...!")

# USING TK TO FRAME
win = Tk()
win.title("login page")
win.geometry('1000x400')
win.config(bg='white')

# HEADING NAME
lala = Label(win, text="USER LOGIN", fg="white", bg="indigo", font="Helvetica 12 bold", width="53", height="3")
lala.place(x=0, y=0)

# NAME OF INPUTS
label = Label(win, text="USERNAME:", fg="tomato", width="10", bg="white")
label.place(x=20, y=100)
label = Label(win, text="PASSWORD:", fg="tomato", width="10", bg="white")
label.place(x=20, y=150)

# INPUTS OF USER DETAIL
var1 = StringVar()
var2 = StringVar()

ent = Entry(win, textvariable=var1, width=50, bg="white", fg="black", show="*")
ent.place(x=120, y=100)
ent = Entry(win, textvariable=var2, width=50, bg="white", fg="black")
ent.place(x=120, y=150)

# SUBMIT BUTTON
btn = Button(win, text="Login", bg="tomato", command=func, font="Helvetica 12 bold", bd="0", width="12", fg="white")
btn.place(x=120, y=200)

# ADDING IMAGE TO RIGHT SIDE
img_path = "D:\Rishi2\login image.png" # Replace with the path of your image file
if os.path.exists(img_path):
    image = PhotoImage(file=img_path)
    image = image.subsample(5)
    image_label = Label(win, image=image,width="500")
    image_label.place(x=500, y=80)

# HOLDING SCREEN
win.mainloop()