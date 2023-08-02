from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame



root = tb.Window(themename="superhero")
root.geometry("700x350")

frame = ScrolledFrame(root)
frame.pack(fill='both', expand=True)

# Label & Button
counter = 0
def changer():
    global counter
    counter += 1
    if counter %2 == 0:
        my_label.config(text="Hey you, don't do this please")
    else:
        my_label.config(text="Hey you, do this please")
my_label = tb.Label(frame, font=("helvetica", 28), bootstyle="danger")
my_label.pack(pady=50)

button = tb.Button(frame, text="click me!", bootstyle="success outline", command=changer)
button.pack(pady=20)


root.mainloop()