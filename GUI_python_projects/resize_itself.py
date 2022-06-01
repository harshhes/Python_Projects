# ------Tkinter GUI Resizing itself--------
from tkinter import *

app = Tk()
app.title("Resizing window")
app.geometry("500x400")


def resize():
    app.geometry(f'{widthentry.get()}x{heightentry.get()}')
    

Label(app, text="Enter Width :", font="lucida 15 bold", pady=20).grid(row=0, column=0)
Label(app, text="Enter Height :", font="lucida 15 bold", pady=20).grid(row=1, column=0)

inputwidth = StringVar()
inputheight = StringVar()


widthentry = Entry(app, textvariable=inputwidth)
widthentry.grid(row=0, column=1)
heightentry = Entry(app, textvariable=inputheight)
heightentry.grid(row=1, column=1)



Button(app, text="Resize", command=resize ).grid(row=2, column=0,padx= 20)

app.mainloop()
