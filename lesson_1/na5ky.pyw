from tkinter import*

root=Tk()
root.geometry("300x150")

fr_top = Frame(root)
fr_bottom = Frame(root)

btn1 = Button(fr_top, text = "Ok_1")
btn2 = Button(fr_top, text = "Ok_2")
btn1.pack(side = "left")
btn2.pack(side = "right")


btn3 = Button(fr_bottom, text = "Ok_3")
btn4 = Button(fr_bottom, text = "Ok_4")
btn3.pack(side = "left")
btn4.pack(side = "right")

fr_top.pack(side = "top", fill = "both")
fr_bottom.pack(side = "bottom",  fill = "both")

root.mainloop()