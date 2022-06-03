from tkinter import *
import pyqrcode
import png
from pyqrcode import QRCode

app = Tk()
app.geometry("600x400")
app.title("Twitter profile QRCode generator")

Label(app, text="Twitter profile QRCode generator!", font='hevetica 30 bold', fg='blue').pack()

Label(app, text="Enter profile link to generate QRCode:", font='lucida 21 bold', fg='black').place(x=100, y=70)

link = StringVar()
Entry(app, textvariable=link,width=50).place(x= 50, y=100)

def twitter():
    url = link.get()
    qrcode = pyqrcode.create(url)
    qrcode.png('test.png', scale=8)
    Label(app, text="QRCode generated sucessfully in file test.png", font='helvetica 20 bold', fg='red').place(x=85, y=200)

Button(app, text="Generate", font='Boulder 20 bold', width=5, relief=SUNKEN, command=twitter).place(x=190, y=130)

app.mainloop()