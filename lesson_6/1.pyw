from tkinter import*
root = Tk()
canv = Canvas(root, width=200, height=100)
canv.pack()
canv.create_oval(30,30,90,90, fill='green')







root.mainloop()