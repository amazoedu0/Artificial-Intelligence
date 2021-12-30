from tkinter import *
import math
import re

expression = ""


def text_box(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equal_to():
    global expression
    # operator = " ".join(re.findall("[\+\-\*\/]+", expression))
    # print(operator)
    # if operator == "+":
    #     total = add()
    # elif operator == "-":
    #     total = subtract()
    # elif operator == "*":
    #     total = mul()
    # elif operator == "/":
    #     total = div()
    # else:
    #     print("Operator not supported")
    # equation.set(total)
    # expression = ""
    result = str(eval(expression))
    equation.set(result)


def clear():
    global expression
    expression = ""
    equation.set("")


def add():
    return str(eval(expression))


def subtract():
    return str(eval(expression))


def mul():
    return str(eval(expression))


def div():
    return str(eval(expression))


def sino():
    global expression
    expression = float(expression)
    expression = round(math.sin(math.radians(expression)), 5)
    equation.set(float(expression))
    expression = str(expression)


def cos():
    return str(eval(expression))


def tan():
    return str(eval(expression))


def log():
    return str(eval(expression))


if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    gui.configure(background="light blue")

    gui.title("Calculator")

    gui.geometry("262x500")

    equation = StringVar()

    expression_field = Entry(gui, textvariable=equation)

    expression_field.grid(columnspan=4, ipadx=70)

    equation.set('0')

    button1 = Button(gui, text=' 1 ', fg='black', bg='red',
                     command=lambda: text_box(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', bg='red',
                     command=lambda: text_box(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='red',
                     command=lambda: text_box(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg='red',
                     command=lambda: text_box(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg='red',
                     command=lambda: text_box(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg='red',
                     command=lambda: text_box(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', bg='red',
                     command=lambda: text_box(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg='red',
                     command=lambda: text_box(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg='red',
                     command=lambda: text_box(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', bg='red',
                     command=lambda: text_box(0), height=1, width=7)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='white', bg='orange',
                  command=lambda: text_box("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='white', bg='orange',
                   command=lambda: text_box("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='white', bg='orange',
                      command=lambda: text_box("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='white', bg='orange',
                    command=lambda: text_box("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='white', bg='green',
                   command=equal_to, height=1, width=7)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='white', bg='grey',
                   command=clear, height=1, width=7)
    clear.grid(row=5, column='1')

    sin = Button(gui, text='sin(', fg='white', bg='grey',
                   command=sino, height=1, width=7)
    sin.grid(row=6, column='0')

    gui.mainloop()
