from tkinter import*
from random import randint, choice

colors = ["#AA99CC","#CCCCCC","#800000", "#00BFFF", "#FF4500", "#00FF00"]
x = 0
y = 0
r =0
points = 0
miss = 0

def new_ball():
    R = randint(10, 40)  # radius
    x = randint(R, 400 - R)
    y = randint(R, 400 - R)
    color = choice(colors)
    canv.create_oval(x-R, y-R, x+R, y+R, fill=color)

def click():
    pass
root = Tk()
root.title("Шаробол")
#root.geometry("800x550")
canv = Canvas(root, width=800, height=550)
canv.pack()
new_ball()

root.config(cursor = "cross_reverse")

root.mainloop()