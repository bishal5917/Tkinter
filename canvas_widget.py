from tkinter import *

root=Tk()

canvas_height=500
canvas_width=800

root.geometry(f"{canvas_width}x{canvas_height}")

canvas_widget=Canvas(root,width=canvas_width,height=canvas_height)
canvas_widget.pack()

canvas_widget.create_line(4,200,300,100,fill="red")

canvas_widget.create_oval(300,2200,56,206,fill="light blue")

# canvas_widget.create_bitmap(300,400,200,800)

root.mainloop()



