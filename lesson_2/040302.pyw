from tkinter import*
root=Tk()
root.geometry("500x100")

btn1=Button(root, text = "Button1")
btn1.grid(row = 0)
ent1=Entry(root)
ent1.grid(row =0, column=2, sticky = W)

btn2=Button(root, text = "Button2", height=2)
btn2.grid(row = 1, column=0)
ent2=Entry(root)
ent2.grid(row =1, column=2, sticky = N)

root.mainloop()