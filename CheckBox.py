from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame

root = tb.Window(themename="superhero")
root.geometry("700x350")

frame = ScrolledFrame(root)
frame.pack(fill='both', expand=True)

var = IntVar()
chck = tb.Checkbutton(frame, text="Checked", bootstyle="primary", variable=var, onvalue=1, offvalue=0)
chck.pack(pady=10)

var1 = IntVar()
chck1 = tb.Checkbutton(frame, text="Checked", bootstyle="success toolbutton", variable=var1, onvalue=1, offvalue=0)
chck1.pack(pady=10)

var2 = IntVar()
chck2 = tb.Checkbutton(frame, text="Checked", bootstyle="warning toggle-round", variable=var2, onvalue=1, offvalue=0)
chck2.pack(pady=10)

var3 = IntVar()
chck3 = tb.Checkbutton(frame, text="Checked", bootstyle="danger toggle-square", variable=var3, onvalue=1, offvalue=0)
chck3.pack(pady=10)

var4 = IntVar()
chck4 = tb.Checkbutton(frame, text="Checked", bootstyle="info toolbutton outline", variable=var4, onvalue=1, offvalue=0, cursor="hand2")
chck4.pack(pady=10)

root.mainloop()