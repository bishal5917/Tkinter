from tkinter import *

root=Tk()

root.geometry("600x500")
def Func():
    global i
    box.insert(ACTIVE,f"{i}")
    i=i+1
i=0
box=Listbox(root)
box.pack()

Button(root,text="keep adding",command=Func).pack()
root.mainloop()
