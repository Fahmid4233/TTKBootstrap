from tkinter import *
from ttkbootstrap.dialogs.colorchooser import ColorChooserDialog
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame


root = tb.Window(themename="superhero")
root.geometry("700x350")
root.state('zoomed')

frame = ScrolledFrame(root)
frame.pack(fill='both', expand=True)

def pick():
    color = ColorChooserDialog()
    color.show()

    results = color.result
    buttons.config(bg=results.hex)

color_btn = tb.Button(frame, text="Choose Color", bootstyle="success outline", command=pick)
color_btn.pack(pady=30)
buttons = Button(frame, width=50, height=20)
buttons.pack(pady=30)

root.mainloop()