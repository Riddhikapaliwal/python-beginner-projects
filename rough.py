from tkinter import *
from tkinter import ttk


def calculate(*args):
    try:
        value=float(feet.get())
        meters.set(round(value*0.3048,4))
    except ValueError :
        pass

root=Tk()
root.title("feets to geometry")

mainframe=ttk.Frame(root,padding=(3,3,12,12))
mainframe.grid(column=0,row=0,sticky=(N,W,E,S))

feet=StringVar()
feet_entry=ttk.Entry(mainframe, width=7 ,textvariable=feet)
feet_entry.grid(column=2,row=1,sticky=(W,E))

meters=StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2,row=2,sticky=(W,E))

ttk.Button(mainframe,text="calculate",command=calculate).grid(column=3,row=3,sticky=W)

ttk.Label(mainframe,text="feet").grid(row=1,column=3,sticky=W)
ttk.Label(mainframe,text="is equivalent to").grid(row=2, column=1,sticky=E)
ttk.Label(mainframe,text="meters").grid(row=2,column=3,sticky=W)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
# mainframe.columnconfigure(2, weight=1)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>",calculate)

root.mainloop()