# Author: Fabian Martinez
# 12/7/2018
# This is a simple gui temperature converter

from tkinter import*
from functools import partial

temperatureValue = 'Celsius'

def storeTempValue(temp):
    global temperatureValue
    temperatureValue = temp

def convert(label1, label2, enteredVar):

    tempNum = enteredVar.get()

    if temperatureValue == 'Celsius':
        fahrenheit = float((tempNum * 9/5) + 32)
        kelvin = float((tempNum + 273.15))
        label1.configure(text='Fahrenheit = ' + str(fahrenheit) + '°F')
        label2.configure(text='kelvin = ' + str(kelvin) + 'K')

    elif temperatureValue == 'Fahrenheit':
        celsius = float((tempNum - 32) * 5/9)
        kelvin = float((tempNum - 32) * 5/9 + 273.15)
        label1.configure(text='Celsius = ' + str(celsius) + '°C')
        label2.configure(text='Kelvin = ' + str(kelvin) + 'K')

    elif temperatureValue == 'Kelvin':
        fahrenheit = float((tempNum - 273.15) * 9/5 + 32)
        celsius = float(tempNum - 273.15)
        label1.configure(text='Fahrenheit = ' + str(fahrenheit) + '°F')
        label2.configure(text='Celsius = ' + str(celsius) + '°C')

    return

root = Tk()
root.geometry('400x200')
root.resizable(0, 0)
root.title('Temp Converter')
root.configure(bg='skyblue')

title = Label(root, text='Temperature Converter', font='arial, 20 bold', bg='skyblue')
title.pack(pady=25, padx=30)

var = IntVar()

entry_box = Entry(root, textvariable=var)
entry_box.place(x=50, y=80, width=200)

optionlist = ['Celsius', 'Kelvin', 'Fahrenheit']
variable = StringVar(root)
variable.set("Celsius")

option = OptionMenu(root, variable, *optionlist, command=storeTempValue)
option.place(x=260, y=75, width=100)


answerlabell = Label(root, anchor=NW, bg='skyblue')
answerlabell.place(x=50, y=105, width=200, height=20)

answerlabel2 = Label(root, anchor=NW, bg='skyblue')
answerlabel2.place(x=50, y=130, width=200, height=20)

getConvert = partial(convert, answerlabell, answerlabel2, var)
button1 = Button(root, text='Convert', command=getConvert)
button1.place(x=260, y=120, width=100)

root.mainloop()