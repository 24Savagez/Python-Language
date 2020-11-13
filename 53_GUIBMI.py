from tkinter import *
import math

def click(event):
    bmi = round(float(textboxWeight.get())/(math.pow(float(textboxHeight.get())/100,2)),1)
    labalBmi.config(text=bmi)
    descBmi(bmi)

def descBmi(bmi):
    if bmi > 30:
        labalDescBmi.config(text="You are Obese")
    elif bmi > 25:
        labalDescBmi.config(text="You are Overweight")
    elif bmi > 18.5:
        labalDescBmi.config(text="You are Smart")
    elif bmi > 16:
        labalDescBmi.config(text="You are Thinness")
    else:
        labalDescBmi.config(text="You are Severe Thinness")

#create a windowsFrom
mainWindows = Tk()

#create a HeightFrom
labalHeight = Label(mainWindows,text="ส่วนสูง(cm.)",font=("Helvetica",12))
labalHeight.grid(row=0,column=0)
textboxHeight = Entry(mainWindows)
textboxHeight.grid(row=0,column=1)

#create a WeightFrom
labalWeight = Label(mainWindows,text="น้ำหนัก(kg.)",font=("Helvetica",12))
labalWeight.grid(row=1,column=0)
textboxWeight = Entry(mainWindows)
textboxWeight.grid(row=1,column=1)

#create a button for calculage Bmi
calButton = Button(mainWindows,text="คำนวน",font=("Helvetica",12))
calButton.grid(row=2,column=0)
calButton.bind('<Button-1>',click)

#show Bmi
labalBmi = Label(mainWindows,text="ผลลัพธ์",font=("Helvetica",12),fg="green")
labalBmi.grid(row=2,column=1)

#show Describtion
labalDescBmi = Label(mainWindows,text="คำอธิบาย",font=("Helvetica",10),fg="magenta")
labalDescBmi.grid(row=3,column=1)

#show windowsFrom
mainWindows.mainloop()

