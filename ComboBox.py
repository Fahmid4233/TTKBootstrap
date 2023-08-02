from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame

root = tb.Window(themename="superhero")
root.geometry("700x350")

frame = ScrolledFrame(root)
frame.pack(fill='both', expand=True)

def check():
    x = combo.get()
    my_label.config(text=x)

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

combo = tb.Combobox(frame, values=days, bootstyle="warning")
combo.pack(pady=30)

my_label = tb.Label(frame)
my_label.pack(pady=10)

button1 = tb.Button(frame, text="Click Here", bootstyle="success outline", command=check)
button1.pack(pady=20)

root.mainloop()