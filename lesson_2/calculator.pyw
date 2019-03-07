from tkinter import*
root=Tk()
root.geometry("210x285")
root.title("Калькулятор")
root.resizable(0,0)#блочим разворот окна

ent2 = Entry(root,width =17, font = "Times 15", justify = RIGHT) #height=2
ent2.grid(row=1,column = 0, columnspan=13,padx = 3, pady=3, ipady=13, ipadx=11)
label1 = Label(root, text = "Калькулятор v1.0") #height=2
label1.grid(row=0,column = 0, columnspan=13,padx = 3, pady=3)
#ent1 = Entry(root)#, font = "Times 19"
#ent1.grid(row=2,padx = 3, pady=3)
#
btn1=Button(root, text = "MC", font = "Times 9",width =3,
height=1)
btn1.grid(row = 3,column =0, padx = 5, pady=3)
btn2=Button(root, text = "MR", font = "Times 9",width =3,
height=1)
btn2.grid(row = 3,column =1, padx = 5, pady=3)
btn3=Button(root, text = "MS", font = "Times 9",width =3,
height=1)
btn3.grid(row = 3,column =2, padx = 5, pady=3)
btn4=Button(root, text = "M+", font = "Times 9",width =3,
height=1)
btn4.grid(row = 3,column =3, padx = 5, pady=3)
btn44=Button(root, text = "M-", font = "Times 9",width =3,
height=1)
btn44.grid(row = 3,column =4, padx = 5, pady=3)

btn5=Button(root, text = "←", font = "Times 9",width =3,
height=1)
btn5.grid(row = 4,column =0, padx = 5, pady=3)
btn6=Button(root, text = "CE", font = "Times 9",width =3,
height=1)
btn6.grid(row = 4,column =1, padx = 5, pady=3)
btn7=Button(root, text = "C", font = "Times 9",width =3,
height=1)
btn7.grid(row = 4,column =2, padx = 5, pady=3)
btn8=Button(root, text = "+/-", font = "Times 9",width =3,
height=1)
btn8.grid(row = 4,column =3, padx = 5, pady=3)
btn9=Button(root, text = "sqrt", font = "Times 9",width =3,
height=1)
btn9.grid(row = 4,column =4, padx = 5, pady=3)

btn9=Button(root, text = "7", font = "Times 9",width =3,
height=1)
btn9.grid(row = 5,column =0, padx = 5, pady=3)
btn10=Button(root, text = 8, font = "Times 9",width =3,
height=1)
btn10.grid(row = 5,column =1, padx = 5, pady=3)
btn11=Button(root, text = "9", font = "Times 9",width =3,
height=1)
btn11.grid(row = 5,column =2, padx = 5, pady=3)
btn12=Button(root, text = "/", font = "Times 9",width =3,
height=1)
btn12.grid(row = 5,column =3, padx = 5, pady=3)
btn121=Button(root, text = "%", font = "Times 9",width =3,
height=1)
btn121.grid(row = 5,column =4, padx = 5, pady=3)

btn13=Button(root, text = "4", font = "Times 9",width =3,
height=1)
btn13.grid(row = 6,column =0, padx = 5, pady=3)
btn14=Button(root, text = "5", font = "Times 9",width =3,
height=1)
btn14.grid(row = 6,column =1, padx = 5, pady=3)
btn15=Button(root, text = "6", font = "Times 9",width =3,
height=1)
btn15.grid(row = 6,column =2, padx = 5, pady=3)
btn16=Button(root, text = "*", font = "Times 9",width =3,
height=1)
btn16.grid(row = 6,column =3, padx = 5, pady=3)
btn161=Button(root, text = "1/x", font = "Times 9",width =3,
height=1)
btn161.grid(row = 6,column =4, padx = 5, pady=3)

btn21=Button(root, text = "1", font = "Times 9",width =3,
height=1)
btn21.grid(row = 7,column =0, padx = 5, pady=3)
btn22=Button(root, text = "2", font = "Times 9",width =3,
height=1)
btn22.grid(row = 7,column =1, padx = 5, pady=3)
btn23=Button(root, text = "3", font = "Times 9",width =3,
height=1)
btn23.grid(row = 7,column =2, padx = 5, pady=3)
btn24=Button(root, text = "-", font = "Times 9",width =3,
height=1)
btn24.grid(row = 7,column =3, padx = 5, pady=3)
btn25=Button(root, text = "=", font = "Times 9",width =3,
height=3)
#btn25.grid(row = 6,column =5, padx = 3, pady=3)
btn25.grid(row = 7,column =4,rowspan=2)
#,sticky = W, padx = 3, pady=3

#btn26=Button(root, text = "0")
#btn26.grid(row = 7,column =1, padx = 3, pady=3)
btn27=Button(root, text = "0", font = "Times 9",width =8,
height=1)
btn27.grid(row = 8,column =0,columnspan=2, padx = 5, pady=3)
btn28=Button(root, text = ",", font = "Times 9",width =3,
height=1)
btn28.grid(row = 8,column =2, padx = 5, pady=3)
btn29=Button(root, text = "+", font = "Times 9",width =3,
height=1)
btn29.grid(row = 8,column =3, padx = 5, pady=3)
#btn30=Button(root, text = "=")
#btn30.grid(row = 7,column =5, padx = 3, pady=3)




root.mainloop()