from tkinter import *

# button = you click it, then it does stuff

def click():
    print("You clicked the button")

window = Tk()

button = Button(window,
                text="click me",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE
                )

button2 = Button(window,
                text="click me2",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE
                )

button.pack()


window.mainloop()