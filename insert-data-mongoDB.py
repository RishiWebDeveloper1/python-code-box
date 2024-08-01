from tkinter import *
# from tkinter import messagebox
from pymongo import MongoClient

myclient = MongoClient()
print(myclient)
db = myclient.testdb

def check_credentials():
    name = username_entry.get()
    password = password_entry.get()

    student_detail = {"name":name, "password":password}
    student_query = db.students.insert_one(student_detail)
    student_query

    # if name == "admin" and password == "password":
    #     messagebox.showinfo("Login Success", "Welcome, admin!")
    # else:
    #     messagebox.showerror("Login Failed", "Invalid username or password")

root = Tk()
root.title("Rishi Login page")
root.geometry("500x300")
root.config(bg="red")

username_label = Label(root, text="Name:")
username_label.place(x=50, y=50)
username_entry = Entry(root)
username_entry.place(x=150, y=50)

password_label = Label(root, text="Password:")
password_label.place(x=50, y=100)
password_entry = Entry(root, show="*")
password_entry.place(x=150, y=100)

login_button = Button(root, text="Login", width=17, bg="purple", fg="white", command=check_credentials)
login_button.place(x=150, y=150)

root.mainloop()
