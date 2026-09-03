import tkinter as tk
from tkinter import messagebox

def login():
    username = username.entry.get()
    password = password.entry.get()
    if username == "admin" and password =="password":
        messagebox.showinfo("Login", "Login successful")
    else:
        messagebox.showerror("Login", "invalid username or password")


root = tk.Tk()
root.title("Login")


# gave something new
