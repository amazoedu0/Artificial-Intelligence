from tkinter import *
import tkinter as tk
import math

expression = ""

inverted = False

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression
        total = eval(expression)
        equation.set(total)
        expression = str(total)

    except:
        equation.set(" Error ")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")
    return


def sqrt():
    global expression
    expression = math.sqrt(float(expression))
    equation.set(float(expression))
    expression = str(expression)


def sin():
    global expression
    expression = float(expression)
    expression = round(math.sin(math.radians(expression)), 5)
    equation.set(float(expression))
    expression = str(expression)


def cos():
    global expression
    expression = float(expression)
    expression = round(math.cos(math.radians(expression)), 5)
    equation.set(float(expression))
    expression = str(expression)


def tan():
    global expression
    expression = float(expression)
    expression = round(math.tan(math.radians(expression)), 5)
    equation.set(float(expression))
    expression = str(expression)


def asin():
    global expression
    expression = float(expression)
    expression = round((math.asin(expression)) * (180 / math.pi), 3)
    equation.set(float(expression))
    expression = str(expression)


def acos():
    global expression
    expression = float(expression)
    expression = round((math.acos(expression)) * (180 / math.pi), 3)
    equation.set(float(expression))
    expression = str(expression)


def atan():
    global expression
    expression = float(expression)
    expression = round((math.atan(expression)) * (180 / math.pi), 3)
    equation.set(float(expression))
    expression = str(expression)


def retrieve_input():
    try:
        global expression
        inputValue1 = InputA.get()
        inputValue2 = InputB.get()
        inputValue1 = float(inputValue1)
        inputValue2 = float(inputValue2)

        expression = float(math.sqrt(inputValue1 * inputValue1 + inputValue2 * inputValue2))
        equation.set(float(expression))
        expression = str(expression)

    except:
        equation.set(" Error ")
        expression = ""

def inv():
    global inverted
    inverted = not inverted


if __name__ == "__main__":
    gui = Tk()

    gui.configure(background="light blue")

    gui.title("Calculator")

    gui.geometry("500x220")

    equation = StringVar()
    A = StringVar()
    B = StringVar()

    expression_field = Entry(gui, textvariable=equation)

    expression_field.grid(columnspan=45, ipadx=200)

    equation.set('Enter Your Expression')

    lbl1 = Label(gui, text="Enter A value:", font=("Arial Bold", 10),
    bg="light blue")
    lbl1.grid(column=0, row=13, sticky=W)
    InputA = Entry(gui, width=12, textvariable=A)
    InputA.grid(column=1, row=13)

    lbl2 = Label(gui, text="Enter B value:", font=("Arial Bold", 10),
    bg="light blue")
    lbl2.grid(column=0, row=14, sticky=W)
    InputB = Entry(gui, width=12, textvariable=B)
    InputB.grid(column=1, row=14)

    buttonab = Button(gui, text=' √(A^2 + B^2) ', fg='black', bg='white',
    command=lambda: retrieve_input(), height=1,width=11)
    buttonab.grid(row=15, column=0, sticky=W + E)

    button1 = Button(gui, text=' 1 ', fg='black', bg='pink',
    command=lambda: press(1), height=1, width=7)
    button1.grid(row=4, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', bg='pink',
    command=lambda: press(2), height=1, width=7)
    button2.grid(row=4, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='pink',
    command=lambda:
    press(3), height=1, width=7)
    button3.grid(row=4, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg='pink',
    command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg='pink',
    command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg='pink',
    command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', bg='pink',
    command=lambda: press(7), height=1, width=7)
    button7.grid(row=2, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg='pink',
    command=lambda: press(8), height=1, width=7)
    button8.grid(row=2, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg='pink',
    command=lambda: press(9), height=1, width=7)
    button9.grid(row=2, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', bg='pink',
    command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=1)

    plus = Button(gui, text=' + ', fg='black', bg='yellow',
    command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='yellow',
    command=lambda:
    press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='yellow',
    command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='yellow',
    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='black', bg='red',
    command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='black', bg='red', command=clear,
    height=1, width=7)
    clear.grid(row=2, column=6)

    sqrt = Button(gui, text=' √ ', fg='black', bg='yellow', command=sqrt,
    height=1, width=7)
    sqrt.grid(row=3, column=6)

    dec = Button(gui, text=' . ', fg='black', bg='orange', command=lambda:
    press("."), height=1, width=7)
    dec.grid(row=5, column=0)

    sin = Button(gui, text='sin', fg='black', bg='light green',
    command=sin, height=1, width=7)
    sin.grid(row=2, column=4)

    cos = Button(gui, text='cos', fg='black', bg='light green',
    command=cos, height=1, width=7)
    cos.grid(row=3, column=4)

    tan = Button(gui, text='tan', fg='black', bg='light green',
    command=tan, height=1, width=7)
    tan.grid(row=4, column=4)

    inv = Button(gui, text='INV', fg='black', bg='light green',
    command=inv, height=1, width=7)
    inv.grid(row=6, column=4)

    if not inverted:
        sin = Button(gui, text='sin', fg='black', bg='light green', command=sin, height=1, width=7)
        sin.grid(row=2, column=4)

        cos = Button(gui, text='cos', fg='black', bg='light green',
        command=cos,
        height=1, width=7)
        cos.grid(row=3, column=4)

        tan = Button(gui, text='tan', fg='black', bg='light green',
        command=tan,
        height=1, width=7)
        tan.grid(row=4, column=4)

    else:
        sin = Button(gui, text='sin^-1', fg='black', bg='light green', command=asin, height=1, width=7)
        sin.grid(row=2, column=4)

        cos = Button(gui, text='cos-1', fg='black', bg='light green',
        command=acos, height=1, width=7)
        cos.grid(row=3, column=4)

        tan = Button(gui, text='tan-1', fg='black', bg='light green',
        command=atan, height=1, width=7)
        tan.grid(row=4, column=4)

gui.mainloop()