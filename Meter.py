from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.dialogs import Messagebox


root = tb.Window(themename="superhero")
root.geometry("700x350")

frame = ScrolledFrame(root)
frame.pack(fill='both', expand=True)

global count
count = 0
def changed():
    global count
    count += 5
    if count <= 100:
        meter1.configure(amountused=count)

    else:
        Messagebox.show_error("Meter is fulled", "Error")

def up():
    meter1.step(10)

def down():
    meter1.step(-10)
meter = tb.Meter(frame,
                 bootstyle="primary",
                 interactive=True,
                 textright='km/h',
                 subtextstyle='success',
                 metertype='semi',
                 amounttotal=180,
                 stripethickness=10,
                 )
meter.pack(pady=20)

meter1 = tb.Meter(frame,
                 bootstyle="primary",
                 subtext="Battery",
                 interactive=True,
                 textright='%',
                 subtextstyle='success',
                 amounttotal=100,
                 amountused=0,
                 # amountused=percent,
                 stripethickness=2,
                 )
meter1.pack(pady=20)

btn = tb.Button(frame, text="Add 5", command=changed, width=15)
btn.pack(pady=20)

btn_1 = tb.Button(frame, text="Step Up", command=up, width=15)
btn_1.pack(pady=20)

btn_2 = tb.Button(frame, text="Step Down", command=down, width=15)
btn_2.pack(pady=20)

root.mainloop()