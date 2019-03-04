from tkinter import*
root=Tk()
root.geometry("500x100")

btn1=Button(root, text = "Button1")
btn1.grid(row = 0)
ent1=Entry(root, width = 20)
ent1.grid(row =0, column=2, sticky = W, pady = 5)

btn2=Button(root, text = "Button2")
btn2.grid(row = 3)
ent2=Entry(root, width = 40)
ent2.grid(row =3, column=2, sticky = N, pady =10)

root.mainloop()