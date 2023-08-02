from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from  ttkbootstrap.dialogs import Querybox


root = tb.Window(themename="superhero")
root.geometry("700x350")

frame = ScrolledFrame(root)
frame.pack(fill='both', expand=True)

def get_dates():
    my_label.config(text=f"You picked {date.entry.get()}")

def dates():
    query = Querybox()
    my_label.config(text=f"You picked {query.get_date()}")
date = tb.DateEntry(frame, bootstyle='success')
date.pack(pady=20)

my_btn = tb.Button(frame, text="Get Date", bootstyle='warning', command=get_dates)
my_btn.pack(pady=20)

my_btn1 = tb.Button(frame, text="Pick Date", bootstyle='danger outline', command=dates)
my_btn1.pack(pady=20)

my_label = tb.Label(frame, text="You picked: ")
my_label.pack()

root.mainloop()