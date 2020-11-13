from tkinter import *

def leftClickButton(event):
    print("Left Click!")
def rightClickButton(event):
    print("Right Click!")
def doubleClickButton(event):
    print("Double Click!")

main = Tk()
button1 = Button(main,text="Click")
button1.pack()
button1.bind('<Button-1>',leftClickButton)
button1.bind('<Button-3>',rightClickButton)
button1.bind('<Double-1>',doubleClickButton)
main.mainloop()