from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame


root = tb.Window(themename="superhero")
root.geometry("700x350")
root.state('zoomed')

frame = ScrolledFrame(root)
frame.pack(fill='both', expand=True)

col = ("first_name", "last_name", "email")
treeview = tb.Treeview(frame, bootstyle="secondary", columns=col)
treeview.pack(pady=20)

treeview.heading(col[0], text="First Name")
treeview.heading(col[1], text="Last Name")
treeview.heading(col[2], text="Email")

contacts = []

for x in range(1,21):
    contacts.append((f"First {x}", f"Last {x}", f"abcd{x}@email.com"))

for contact in contacts:
    treeview.insert('', END, values=contact)

root.mainloop()