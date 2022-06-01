from tkinter import *
import tkinter.messagebox as tmsg

app_window = Tk()
app_window.title("Radio button Window")
app_window.geometry("600x350")

def order():
   tmsg.showinfo("Recieved", f"We have recieved your order for {var.get()}. Thanks for ordering with us!")
   

var = StringVar()
var.set('Radio')
Label(app_window, text="What would you like to have sir?", font = 'lucida 25 bold' ).pack()

dish = ['Dosa', 'Pizza', 'Idli', 'Pasta']
for i in dish:
    radio = Radiobutton(app_window, text=f'{i}', padx=15, variable=var,
    value=f"{i}").pack(anchor="w",padx=25,pady=5)

Button(text="Order Now", command=order).pack()

app_window.mainloop()