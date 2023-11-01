from tkinter import *

# button = you click it, then it does stuff

def click():
    print("You clicked the button")

window = Tk()

button = Button(window,
                text="click me",
                command=click,
                font=("Comic Sans", 30))

button.pack()


window.mainloop()