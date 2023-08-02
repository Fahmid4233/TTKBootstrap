from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame



root = tb.Window(themename="superhero")
root.geometry("700x350")

frame = ScrolledFrame(root)
frame.pack(fill='both', expand=True)

tb.Entry(frame, bootstyle="dark", font=("Helvetica", 16, 'bold')).pack(pady=20)

root.mainloop()