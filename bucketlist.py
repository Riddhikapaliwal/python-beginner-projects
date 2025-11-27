from tkinter import *
from tkinter import messagebox


root=Tk()
root.title("BucketList")
root.configure(bg="brown")
root.geometry("400x400")
frame1=Frame(root,bg="wheat",height=150,width=400)
frame1.pack(padx=5, pady=5,anchor="w")

frame1.pack_propagate(False)



frame2=Frame(root,bg="wheat",height=250,width=400)
frame2.pack(padx=5, pady=5,anchor="w")

canvas = Canvas(frame2, bg="wheat")
scrollbar = Scrollbar(frame2, orient=VERTICAL, command=canvas.yview)
scrollable_frame = Frame(canvas, bg="wheat")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill=Y)


def clear():
    for widgets in scrollable_frame.winfo_children():
        widgets.destroy()

def add():
    value=entry.get().strip()
    var = IntVar()
    chklist.append(var)
    if value=="":
        messagebox.showinfo("empty","enter something")
        return
    else:
        chbx=Checkbutton(scrollable_frame,text=value,variable=var,bg="brown",font=("Arial", 15,"bold"),width=400,anchor="w")
        chbx.pack(anchor="w",pady=2 )
        entry.delete(0,END)

label=Label(frame1, text="-- enter items --",bg="wheat",fg="brown", font=("Arial", 20,"italic"))
label.pack()
entry=Entry(frame1,borderwidth=4 , font=("Arial", 20),bg="wheat")
entry.pack()

chklist=[]

btn1=Button(frame1,text="Add",width=20,command=add,bg="brown",fg="wheat")
btn1.pack(side=LEFT,padx=10,pady=10)

btn2=Button(frame1,text="Clear all",width=20,command=clear,bg="brown",fg="wheat")
btn2.pack(side=RIGHT,padx=10,pady=10)

root.resizable(False,False)
entry.focus()
root.mainloop()