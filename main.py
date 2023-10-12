import tkinter
from tkinter import *

screen = tkinter.Tk()
screen.title("BMI Calculator")
screen.minsize(width=300,height=300)




def click_calculate():
    kilo1 = entry1.get()
    boy2 = entry2.get()
    try:
        kilo = float(kilo1)
        boy = float(boy2) /100
        bmi = kilo / (boy * boy)
        if bmi < 18.5:
            label3.config(text="You are underweight!", font=20)

        elif 18.50 < bmi < 25:
            label3.config(text="You are normal weight!", font=20)
        elif 25 < bmi < 30:
            label3.config(text="You are overweight!", font=20)
        else:
            label3.config(text="You are obese", font=20)
    except ValueError:
        label3.config(text="Please Enter a Number!", font=20)
    label3.config()



label1 = tkinter.Label(text="Your Weight (kg)",font=20)
label1.pack()

entry1 = tkinter.Entry(width=20)
entry1.pack()


label2 = tkinter.Label(text="Your length (cm)", font=20)
label2.pack()


entry2 = tkinter.Entry(width=20)
entry2.pack()


button = tkinter.Button(text="Calculate",command=click_calculate)
button.pack()

label3 = tkinter.Label(text="",)
label3.pack()







tkinter.mainloop()



