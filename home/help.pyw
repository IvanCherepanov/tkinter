from tkinter import *
from random import randint, choice
clicks = 0
colors = ["#AA99CC","#CCCCCC","#800000", "#00BFFF", "#FF4500", "#00FF00"]
x = 0
y = 0
r =0
points = 0
miss = 0
def new_ball():
    R = randint(10, 40)  # radius
    x = randint(R, 300 - R)
    y = randint(R, 300 - R)
    color = choice(colors)
    canv.create_oval(x-R, y-R, x+R, y+R, fill=color, command=click_button)

def click_button():
    global clicks
    clicks += 1
    root.title("Clicks {}".format(clicks))
 
root = Tk()
root.title("GUI на Python")
root.geometry("300x550")

#btn = Button( width = 300, height = 550, background="#555", foreground="#ccc",
#             padx="20", pady="8", font="16", command=click_button)
#btn.pack()
canv = Canvas(root, width=300, height=550)
canv.pack()
new_ball()
 


 
root.mainloop()