from tkinter import *

root=Tk()

root.geometry("600x500")
def Func():
    for i in range(80):
        box.insert(ACTIVE,f"{i}")
        i=i+1
i=0
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
box=Listbox(root,yscrollcommand=scrollbar.set)
box.pack()
scrollbar.config(command=box.yview)
Button(root,text="keep adding",command=Func).pack()
root.mainloop()