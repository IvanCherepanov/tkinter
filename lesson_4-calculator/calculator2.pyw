from tkinter import*
import math

def number_button(num):
    text1.insert(END, str(num))

"""def clear():
    text.delete(0,END)"""

root = Tk()
root.title("Калькулятор")
root.resizable(0,0)

frame1=Frame(root)
frame1.pack(side  = TOP, pady=5)

frame2=Frame(root)
frame2.pack(side  = LEFT, anchor = N, pady=5, padx = 5)

text1 = Entry(frame1, font="Arial 30", justify = "right", bd = 20, insertwidth=-1)
text1.pack(side = RIGHT, anchor = N)

b_b = Button(frame2, text = "n!", width = 3, bd = 8, fg = "red", font="Arial 30" )
b_b.grid(row=1, column=1)
b_ce = Button(frame2, text = "CE", width = 3, bd = 8, fg = "red", font="Arial 30" )
b_ce.grid(row=1, column=2)
b_c = Button(frame2, text = "C", width = 3, bd = 8, fg = "red", font="Arial 30" )
b_c.grid(row=1, column=3)
b_sqrt = Button(frame2, text = "sqrt", width = 3, bd = 8, fg = "red", font="Arial 30" )
b_sqrt.grid(row=1, column=4)
b_st = Button(frame2, text = "^", width = 3, bd = 8, fg = "red", font="Arial 30" )
b_st.grid(row=1, column=5)

b_7 = Button(frame2, text = "7", width = 3, bd = 8, fg = "red", font="Arial 30" )
b_7.grid(row=2, column=1)
b_8 = Button(frame2, text = "8", width = 3, bd = 8, fg = "red", font="Arial 30" )
b_8.grid(row=2, column=2)
b_9 = Button(frame2, text = "9", width = 3, bd = 8, fg = "red", font="Arial 30" )
b_9.grid(row=2, column=3)
b_div = Button(frame2, text = "/", width = 3, bd = 8, fg = "red", font="Arial 30" )
b_div.grid(row=2, column=4)
b_left = Button(frame2, text = "(", width = 3, bd = 8, fg = "red", font="Arial 30" )
b_left.grid(row=2, column=5)

b_4 = Button(frame2, text = "4", width = 3, bd = 8, fg = "red", font="Arial 30" )
b_4.grid(row=3, column=1)
b_5 = Button(frame2, text = "5", width = 3, bd = 8, fg = "red", font="Arial 30" )
b_5.grid(row=3, column=2)
b_6 = Button(frame2, text = "6", width = 3, bd = 8, fg = "red", font="Arial 30" )
b_6.grid(row=3, column=3)
b_multi = Button(frame2, text = "*", width = 3, bd = 8, fg = "red", font="Arial 30" )
b_multi.grid(row=3, column=4)
b_right = Button(frame2, text = ")", width = 3, bd = 8, fg = "red", font="Arial 30" )
b_right.grid(row=3, column=5)

b_1 = Button(frame2, text = "1", width = 3, bd = 8, fg = "red", font="Arial 30" )
b_1.grid(row=4, column=1)
b_8 = Button(frame2, text = "2", width = 3, bd = 8, fg = "red", font="Arial 30" )
b_8.grid(row=4, column=2)
b_9 = Button(frame2, text = "3", width = 3, bd = 8, fg = "red", font="Arial 30" )
b_9.grid(row=4, column=3)
b_div = Button(frame2, text = "-", width = 3, bd = 8, fg = "red", font="Arial 30" )
b_div.grid(row=4, column=4)
b_eq = Button(frame2, text = "=", width = 3, height = 3, bd = 8, fg = "red", font="Arial 30" )
b_eq.grid(row=4, column=5, rowspan = 2)

b_0 = Button(frame2, text = "0", width = 8, bd = 8, fg = "red", font="Arial 30" )
b_0.grid(row=5, column=1, columnspan = 2)
b_ = Button(frame2, text = ",", width = 3, bd = 8, fg = "red", font="Arial 30" )
b_.grid(row=5, column=3)
b_plus = Button(frame2, text = "+", width = 3, bd = 8, fg = "red", font="Arial 30" )
b_plus.grid(row=5, column=4)



root.mainloop()