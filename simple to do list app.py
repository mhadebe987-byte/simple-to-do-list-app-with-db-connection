import mysql.connector
from tkinter import *
from tkinter import messagebox
import time

# Connect to database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mzamo1010H!",
    database="tasks_db"
)
mycursor = db.cursor()

# Function to add user entry into the listbox
def add():
    info = entry.get()
    if info.strip() == "":
        messagebox.showerror("Error", "Task cannot be empty!")
        return
    mycursor.execute("INSERT INTO tasks (description) VALUES (%s)", (info,))
    db.commit()
    textbox.insert(END, info)
    entry.delete(0, END)

# Function to remove a task inside the listbox    
def delete():
    try:
        selected_index = textbox.curselection()[0]
        info = textbox.get(selected_index)
        textbox.delete(selected_index)
        mycursor.execute("DELETE FROM tasks WHERE description = %s", (info,))
        db.commit()
        today = time.asctime()
        messagebox.showinfo("Deleted", f"Task '{info}' deleted at {today}")
    except IndexError:
        messagebox.showerror("Error", "Pick something to delete!")

# Initiating the program (GUI)
app = Tk()
app.geometry("600x600")
app.title("To Do List App")
app.config(bg="black")

cap = Label(app, text="Welcome To Do List App", font=("bold", 20), bg="black", fg="white")
cap.grid(row=0, columnspan=2)

# Used to store users tasks
textbox = Listbox(app, width=90, height=20)
textbox.grid(row=1, column=0, columnspan=2)

# Accepts user task and stores it in the listbox
entry = Entry(app, width=40)
entry.grid(row=2, column=0, columnspan=2)

# Buttons
addbtn = Button(app, text="Add", fg="red", bg="orange", command=add)
addbtn.grid(row=3, column=0)

delbtn = Button(app, text="Delete", fg="red", bg="orange", command=delete)
delbtn.grid(row=3, column=1)

# Start the program
app.mainloop()
