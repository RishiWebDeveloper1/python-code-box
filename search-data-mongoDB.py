from tkinter import *
# from tkinter import messagebox
from pymongo import MongoClient

myclient = MongoClient()
print(myclient)
db = myclient.testdb

def check_credentials():
    name = search_entry.get()

    if (name == ""):
        student_query = db.students.find()
        data = ""
        for student in student_query:
            p = f"{student["name"]} = {student["password"]} \n"
            data += p
        result_label.config(text=data)
    else:
        student_get_data = db.students.find_one({"name":name})
        print(student_get_data)
        if student_get_data == "None":
            result_label.config(text="Data not found!")
        else:
            p = student_get_data["name"], student_get_data["password"]
            result_label.config(text=p)


root = Tk()
root.title("Rishi Login page")
root.geometry("500x300")
root.config(bg="red")

search_entry = Entry(root)
search_entry.place(x=150, y=100)

login_button = Button(root, text="Search", width=17, bg="purple", fg="white", command=check_credentials)
login_button.place(x=150, y=150)

result_label = Label(root, text="None", bg="red", fg="white")
result_label.place(x=50, y=200)

root.mainloop()
