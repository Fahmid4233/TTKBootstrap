from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame


root = tb.Window(themename="superhero")
root.geometry("700x350")

frame = ScrolledFrame(root)
frame.pack(fill='both', expand=True)

def order():
    label2.config(text=f"You Ordered: {radio.get()}")
foods = ['Pasta', 'Burger', 'Pizza', 'Drinks', 'Tea', "Coffee"]
radio = StringVar()
for food in foods:
    tb.Radiobutton(frame, bootstyle='danger', variable=radio, text=food, value=food, command=order).pack(pady=20)

btn_6 = tb.Button(frame, text="Order")
btn_6.pack(pady=20)

label2 = tb.Label(frame, text="You Ordered: ")
label2.pack()

root.mainloop()