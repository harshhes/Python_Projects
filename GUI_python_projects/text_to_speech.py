from tkinter import *
from playsound import playsound
from gtts import gTTS

app = Tk()
app.title("Text To Speech GUI")
app.geometry("600x400")

Label(app, text="TEXT TO SPEECH GUI", font='helvetica 30 bold',).pack()
Label(app, text="Enter text: ", font='lucida 22 bold',).place(x=200, y=60)

text = StringVar()

textentry = Entry(app, textvariable=text, width =40)
textentry.place(x=100, y=95)

def tts():
    message = textentry.get()
    speech = gTTS(text=message)
    speech.save("text1.mp3")
    playsound("text1.mp3")

def exit():
    app.destroy()

def reset():
    text.set('')

Button(app,text="Play", font='helvetica 15 bold', command=tts, width = 8).place(x= 100, y=130)
Button(app, text="Exit", font = 'helvetica 15 bold', command=exit, bg='black',fg='red').place(x=220,y=130)
Button(app, text="Reset", font = 'helvetica 15 bold', command=reset, fg='blue').place(x=290,y=130)

app.mainloop()
