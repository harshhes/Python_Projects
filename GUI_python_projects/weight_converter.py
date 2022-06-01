# WEIGHT CONVERTER GUI
from tkinter import *

app = Tk()


def convert():
    gram = float(weightvalue.get())*1000
    pound = float(weightvalue.get())*2.20
    ounce = float(weightvalue.get())*35.27
    t1.delete("1.0", END)
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END, pound)
    t3.delete("1.0", END)
    t3.insert(END, ounce)


app.title("Weight Converter")
app.geometry("600x400")

weight = Label(app, text="Enter the weight in Kgs: ", font="Bold 15 bold")
weight.grid()

weightvalue = StringVar()

weightentry = Entry(app,textvariable=weightvalue)
weightentry.grid(row=0, column=1,)

weightbutton = Button(app,text="Convert",command=convert)
weightbutton.grid(row=0, column=2, padx= 20)

w1 = Label(app, text="Gram")
w2 = Label(app, text="Pound")
w3 = Label(app, text="Ounce")

t1 = Text(app, height =10, width =30)
t2= Text(app, height =10, width=30)
t3= Text(app, height =10, width=30)

w1.grid(row=1, column=0)
w2.grid(row=1, column=1)
w3.grid(row=1, column=2)

t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)


app.mainloop()