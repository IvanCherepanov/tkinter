from tkinter import*
from random import randint, choice

def draw_1_circle_count_red(event):
    count = 0
    for i in range(20):
        R = randint(10, 40)  # radius
        x = randint(R, 400 - R)
        y = randint(R, 400 - R)
        color = choice(colors)
        canv.create_oval(x-R, y-R, x+R, y+R, fill=color)
        if color == "red" and R<20 or color =="green" and R>50:
            count +=1
    print(count,"circle(s)")
        
    
root = Tk()
#root.geometry("800x600")
fr = Frame(root)
btn1=Button(fr, text='Draw and Count')
btn1.pack(side=LEFT)
btn1.bind('<1>', draw_1_circle_count_red)

fr.pack()

colors=['green', 'blue', 'red', '#BB99ff', '#FF00CC']


canv = Canvas(root, width=400, height=400)
canv.pack()
#canv.create_oval(30,30,90,90, fill='green')
#btn1.bind("<Button-1>", draw_1_circle_count_red)

root.mainloop()