# сделать так, чтобы кнопка 4 была около снопки 2 по ветрикали
from tkinter import*

root=Tk()

root.geometry("400x400")


fr_top = Frame(root)
fr_bottom = Frame(root)
fr_bottom_bottom = Frame(root)

btn1 = Button(fr_top, text = "1", padx="5")
btn3 = Button(fr_top, text = "3", padx="5")
btn1.pack(side = "left")
btn3.pack(side = "right")


btn2 = Button(fr_bottom, text = "2", padx="5")
btn2.pack(side = "right",  fill = "both")

btn4 = Button(fr_bottom_bottom, text = "4", padx="5")
btn5 = Button(fr_bottom_bottom, text = "5", padx="5")
btn4.pack(side = "right")

btn5.pack(side = "right", padx = 139)

fr_top.pack(side = "top", fill = "both")
fr_bottom.pack(anchor = "center")
fr_bottom_bottom.pack(side = "bottom", fill  = "both")
root.mainloop()