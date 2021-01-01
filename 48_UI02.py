from tkinter import *


def sayHello():
    print("Hello World")


def helpMe():
    print("What the heck")


# mainWindows
mainWindows = Tk()
# button
button = Button(mainWindows, text="Click Me1", command=sayHello).grid(row=0, column=1)
button2 = Button(mainWindows, text="Click Me2", command=sayHello).grid(row=0, column=2)
button3 = Button(mainWindows, text="Click Me3", command=helpMe).grid(row=1, column=1)

# show
mainWindows.mainloop()
