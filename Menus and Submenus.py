from tkinter import *

root=Tk()
root.geometry("600x400")

def tfunc():
    print("huhf")

# first menu
mainmenu=Menu(root)

m1=Menu(mainmenu,tearoff=0)

m1.add_command(label="New",command=tfunc)
m1.add_command(label="open",command=tfunc)
m1.add_separator()
m1.add_command(label="save",command=tfunc)
m1.add_command(label="save as",command=tfunc)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)

m2=Menu(mainmenu)
m2.add_command(label="exit",command=quit)

mainmenu.add_cascade(label="exit",command=quit)
root.mainloop()
