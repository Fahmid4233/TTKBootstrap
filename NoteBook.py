from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame


root = tb.Window(themename="superhero")
root.geometry("700x350")

frame = ScrolledFrame(root)
frame.pack(fill='both', expand=True)

note_book = tb.Notebook(frame, bootstyle='dark')
note_book.pack(pady=20, expand=True, fill=BOTH)

tab1 = tb.Frame(note_book)
tab2 = tb.Frame(note_book)

my_label1 = tb.Label(tab1, text="First Tab")
my_label1.pack(padx=20, pady=20)

text1 = tb.Text(tab1)
text1.pack()

my_label2 = tb.Label(tab2, text="Second Tab")
my_label2.pack(padx=20, pady=20)

text2 = tb.Text(tab2)
text2.pack()

note_book.add(tab1, text="Tab1")
note_book.add(tab2, text="Tab2")

root.mainloop()