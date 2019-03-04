from tkinter import*
root=Tk()
root.geometry("500x150")


btn1=Button(root, text = "Button1")
btn1.grid(row = 0,column =1, padx = 3, pady=3)
btn2=Button(root, text = "Button2")
btn2.grid(row = 0,column =2, padx = 3, pady=3)
btn3=Button(root, text = "Button3")
btn3.grid(row = 0,column =3, padx = 3, pady=3)
btn4=Button(root, text = "Button4")
btn4.grid(row = 0,column =4, padx = 3, pady=3)

btn5=Button(root, text = "Button5")
btn5.grid(row = 1,column =1, padx = 3, pady=3)
btn6=Button(root, text = "Button6")
btn6.grid(row = 1,column =2, padx = 3, pady=3)
btn7=Button(root, text = "Button7")
btn7.grid(row = 1,column =3, padx = 3, pady=3)
btn8=Button(root, text = "Button8")
btn8.grid(row = 1,column =4, padx = 3, pady=3)

btn9=Button(root, text = "Button9")
btn9.grid(row = 2,column =1, padx = 3, pady=3)
btn10=Button(root, text = "Button10")
btn10.grid(row = 2,column =2, padx = 3, pady=3)
btn11=Button(root, text = "Button11")
btn11.grid(row = 2,column =3, padx = 3, pady=3)
btn12=Button(root, text = "Button12")
btn12.grid(row = 2,column =4, padx = 3, pady=3)

btn13=Button(root, text = "Button13")
btn13.grid(row = 3,column =1, padx = 3, pady=3)
btn14=Button(root, text = "Button14")
btn14.grid(row = 3,column =2, padx = 3, pady=3)
btn15=Button(root, text = "Button15")
btn15.grid(row = 3,column =3, padx = 3, pady=3)
btn16=Button(root, text = "Button16")
btn16.grid(row = 3,column =4, padx = 3, pady=3)

ent1=Entry(root, width = 40)
ent1.grid(row =4, column=  1, columnspan =4) #, sticky = S

"""btn2=Button(root, text = "Button2")
btn2.grid(row = 3)
ent2=Entry(root, width = 40)
ent2.grid(row =3, column=2, sticky = N, pady =10)"""


root.mainloop()