from tkinter import *


def hello():
    print("Hello What is your name")


mainWindows = Tk()
text1 = Label(mainWindows, text="Hello", width=20, fg="red", bg="black", font=("Helvetica", 38), anchor=W).grid(row=0,
                                                                                                                column=1)
button1 = Button(mainWindows, text="Click", command=hello, width=20, fg="white", bg="gray").grid(row=1, column=1)

mainWindows.mainloop()
