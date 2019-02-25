from tkinter import*
root=Tk()
root.geometry("150x100")
btn1 = Button(root, text = "Button1")
btn1.pack(side = "left")
btn2 = Button(root, text = "Button2")
btn2.pack(side = "right", anchor = "sw")
root.mainloop()