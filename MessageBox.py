from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.dialogs import Messagebox


root = tb.Window(themename="superhero")
root.geometry("700x350")
root.state('zoomed')

frame = ScrolledFrame(root)
frame.pack(fill='both', expand=True)

def yesno():
    Messagebox.yesno("Yesno", "Message")

def ok():
    Messagebox.ok("Ok", "Message")

def okcancel():
    Messagebox.okcancel("Ok Cancel", "Message")

def show_info():
    Messagebox.show_info("Show Info", "Message")

def show_error():
    Messagebox.show_error("Show Error", "Message")

def show_warning():
    Messagebox.show_warning("Show Warning", "Message")

def show_ques():
    Messagebox.show_question("Show Question", "Message")

def retrycancel():
    Messagebox.retrycancel("Retry Cancel", "Message")

msg_btn = tb.Button(frame, text="yesno", command=yesno)
msg_btn.pack(pady=20)

msg_btn1 = tb.Button(frame, text="okcancel", command=okcancel)
msg_btn1.pack(pady=20)

msg_btn2 = tb.Button(frame, text="show_info", command=show_info)
msg_btn2.pack(pady=20)

msg_btn3 = tb.Button(frame, text="show_error", command=show_error)
msg_btn3.pack(pady=20)

msg_btn4 = tb.Button(frame, text="show_question", command=show_ques)
msg_btn4.pack(pady=20)

msg_btn5 = tb.Button(frame, text="show_warning", command=show_warning)
msg_btn5.pack(pady=20)

msg_btn6 = tb.Button(frame, text="retrycancel", command=retrycancel)
msg_btn6.pack(pady=20)

root.mainloop()