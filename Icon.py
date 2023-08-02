from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.icons import Icon


root = tb.Window(themename="superhero")
root.geometry("700x350")

frame = ScrolledFrame(root)
frame.pack(fill='both', expand=True)

img = PhotoImage(data=Icon.icon)
img1 = PhotoImage(data=Icon.warning)
img2 = PhotoImage(data=Icon.info)
img3 = PhotoImage(data=Icon.error)
img4 = PhotoImage(data=Icon.question)

icon1 = tb.Label(frame, image=img)
icon1.pack(pady=10)

icon2 = tb.Label(frame, image=img1)
icon2.pack(pady=10)

icon3 = tb.Label(frame, image=img2)
icon3.pack(pady=10)

icon4 = tb.Label(frame, image=img3)
icon4.pack(pady=10)

icon5 = tb.Label(frame, image=img4)
icon5.pack(pady=10)

root.mainloop()