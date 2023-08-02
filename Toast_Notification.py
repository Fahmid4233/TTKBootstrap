from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification


root = tb.Window(themename="superhero")
root.geometry("700x350")

frame = ScrolledFrame(root)
frame.pack(fill='both', expand=True)

def notification():
    Toast.show_toast()

Toast = ToastNotification(title="Notification", message="Hello buddy", duration=3000, alert=True, icon="PyCharm")

tst_btn = tb.Button(frame, bootstyle='warning outline', text="Show Notification", command=notification)
tst_btn.pack()

root.mainloop()