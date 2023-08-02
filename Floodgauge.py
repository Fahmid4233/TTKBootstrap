from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame

root = tb.Window(themename="superhero")
root.geometry("700x350")

frame = ScrolledFrame(root)
frame.pack(fill='both', expand=True)

def start():
    footgauge.start()

def stop():
    footgauge.stop()

def inc():
    footgauge.step(20)
footgauge = tb.Floodgauge(frame, mask="{}%", bootstyle="primary",orient="horizontal", maximum=100, value=0)
footgauge.pack(pady=20, padx=20)
start_btn = tb.Button(frame, text="start", bootstyle="secondary", command=start)
start_btn.pack(pady=5)

pause_btn = tb.Button(frame, text="Pause", bootstyle="success", command=stop)
pause_btn.pack(pady=5)

increment_btn = tb.Button(frame, text="Increment", bootstyle="primary", command=inc)
increment_btn.pack(pady=5)

root.mainloop()