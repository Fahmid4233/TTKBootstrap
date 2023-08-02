from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.dialogs.dialogs import FontDialog


root = tb.Window(themename="superhero")
root.geometry("700x350")

frame = ScrolledFrame(root)
frame.pack(fill='both', expand=True)

def font():
    font = FontDialog()
    font.show()

    lab.config(font=font.result)

font_btn = tb.Button(frame, text="Font", bootstyle="secondary outline", command=font)
font_btn.pack(pady=20)

lab = tb.Label(frame, text="Hello World!")
lab.pack(pady=40)

root.mainloop()