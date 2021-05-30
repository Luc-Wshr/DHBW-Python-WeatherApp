import tkinter
from tkinter import messagebox
# hide main window
root = tkinter.Tk()
# message box display
messagebox.showerror("Error", "Error message")
messagebox.showwarning("Warning","Warning message")
messagebox.showinfo("Information","Informative message")