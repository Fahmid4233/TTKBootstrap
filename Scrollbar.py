from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame



root = tb.Window(themename="superhero")
root.geometry("700x350")

frame = ScrolledFrame(root)
frame.pack(fill='both', expand=True)

scroll_frame = ScrolledFrame(frame, autohide=False, bootstyle="light")
scroll_frame.pack()

for x in range(50):
    tb.Label(scroll_frame, bootstyle='info', text="Clicked").pack(pady=10)

root.mainloop()