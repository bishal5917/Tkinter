from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()

root.geometry("600x400")

Label(root,text="Rate us out of 10 !").pack()
slider=Scale(root,from_=0,to=10,orient=HORIZONTAL)
slider.pack()


root.mainloop()
