from tkinter import *

def sayHello():
    print("Hello World")
def helpMe():
    print("What the heck")
#mainWindows
mainWindows = Tk()
#button
button = Button(mainWindows,text = "Click Me",command = sayHello)
button.place(x=70 , y=50)
#show main
mainWindows.mainloop()

mainWindows2 = Tk()
button2 = Button(mainWindows2,text = "Help",command = helpMe)
button2.place(x=70, y=80)
mainWindows2.mainloop()