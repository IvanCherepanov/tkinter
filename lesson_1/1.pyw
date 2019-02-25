from tkinter import*
root=Tk()
root.geometry("150x100")
fr1 = Frame(root)
fr1.pack(side =TOP)
btn1 = Button(fr1, text = "Button1")
btn1.pack(side = "left")
btn2 = Button(fr1, text = "Button1")
btn2.pack(side = "right", padx = 5)
"""btn1 = Button(root, text = "Button1")
btn1.pack(side = "left")
btn2 = Button(root, text = "Button2")
btn2.pack(side = "right", anchor = "sw")"""
root.mainloop()