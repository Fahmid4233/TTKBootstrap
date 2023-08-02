from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame

root = tb.Window(themename="superhero")
root.geometry("700x350")

frame = ScrolledFrame(root)
frame.pack(fill='both', expand=True)

def slide(e):
    my_label3.config(text=f"{int(slider.get())}")
slider = tb.Scale(frame, bootstyle='success', length=200, from_=0, to=100, command=slide)
slider.pack(pady=40)

my_label3 = tb.Label(frame, font=("Helvetica", 28, 'bold'))
my_label3.pack(pady=20)

root.mainloop()