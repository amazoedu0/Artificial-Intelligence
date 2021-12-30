from tkinter import *
import math

def btnClick(number):
    global value
    value=value+str(number)
    data.set(value)

def btnClear():
    global value
    value=""
    data.set(value)

def btnEquals():
    global value
    result = str(eval(value))
    data.set(result)

def btnSIN():
    global value
    value = float(value)
    value = round(math.sin(value), 5)
    data.set(float(value))
    value = str(value)

def btnCOS():
    global value
    value = float(value)
    value = round(math.cos(math.radians(value)), 5)
    data.set(float(value))
    value = str(value)

def btnTAN():
    global value
    value = float(value)
    value = round(math.tan(math.radians(value)), 5)
    data.set(float(value))
    value = str(value)

def btnLOG():
    global value
    value = float(value)
    value = round(math.log(value), 5)
    data.set(float(value))
    value = str(value)


value=""

root = Tk()
root.title("Simple Calculator")
root.geometry("360x380+100+400")
data = StringVar()
display = Entry(root, textvariable=data, bd=30, justify="right", bg="powder blue", font=("Ariel", 20, "bold"))
display.grid(row=0, columnspan=4)


btn7=Button(root,text="7",font=("Ariel",12,"bold"), bg="orange",height=2, width=6, command = lambda: btnClick(7))
btn7.grid(row=1,column=0)
btn8=Button(root,text="8",font=("Ariel",12,"bold"), bg="orange",height=2, width=6, command = lambda: btnClick(8))
btn8.grid(row=1,column=1)
btn9=Button(root,text="9",font=("Ariel",12,"bold"), bg="orange",height=2, width=6, command = lambda: btnClick(9))
btn9.grid(row=1,column=2)
btn_add=Button(root,text="+",font=("Ariel",12,"bold"), bg="purple",fg="white",height=2, width=6, command = lambda: btnClick('+'))
btn_add.grid(row=1,column=3)

btn4=Button(root,text="4",font=("Ariel",12,"bold"), bg="orange",height=2, width=6, command = lambda: btnClick(4))
btn4.grid(row=2,column=0)
btn5=Button(root,text="5",font=("Ariel",12,"bold"), bg="orange",height=2, width=6, command = lambda: btnClick(5))
btn5.grid(row=2,column=1)
btn6=Button(root,text="6",font=("Ariel",12,"bold"), bg="orange",height=2, width=6, command = lambda: btnClick(6))
btn6.grid(row=2,column=2)
btn_sub=Button(root,text="-",font=("Ariel",12,"bold"),bg="purple",fg="white",height=2, width=6, command = lambda: btnClick('-'))
btn_sub.grid(row=2,column=3)

btn1=Button(root,text="1",font=("Ariel",12,"bold"), bg="orange",height=2, width=6, command = lambda: btnClick(1))
btn1.grid(row=3,column=0)
btn2=Button(root,text="2",font=("Ariel",12,"bold"), bg="orange",height=2, width=6, command = lambda: btnClick(2))
btn2.grid(row=3,column=1)
btn3=Button(root,text="3",font=("Ariel",12,"bold"), bg="orange",height=2, width=6, command = lambda: btnClick(3))
btn3.grid(row=3,column=2)
btn_mul=Button(root,text="x",font=("Ariel",12,"bold"), bg="purple",fg="white",height=2, width=6, command = lambda: btnClick('*'))
btn_mul.grid(row=3,column=3)

btn_cancel=Button(root,text="C",font=("Ariel",12,"bold"), bg="red",height=2, width=6, command = btnClear)
btn_cancel.grid(row=4,column=0)
btn0=Button(root,text="0",font=("Ariel",12,"bold"), bg="orange",height=2, width=6, command = lambda: btnClick(0))
btn0.grid(row=4,column=1)
btn_equal=Button(root,text="=",font=("Ariel",12,"bold"), bg="green",fg="white",height=2, width=6, command = btnEquals)
btn_equal.grid(row=4,column=2)
btn_div=Button(root,text="/",font=("Ariel",12,"bold"), bg="purple",fg="white",height=2, width=6, command = lambda: btnClick('/'))
btn_div.grid(row=4,column=3)

btn_sin=Button(root,text="SIN",font=("Ariel",12,"bold"), bg="lightblue",height=2, width=6, command = btnSIN)
btn_sin.grid(row=5,column=0)
btn_cos=Button(root,text="COS",font=("Ariel",12,"bold"), bg="lightblue",height=2, width=6, command = btnCOS)
btn_cos.grid(row=5,column=1)
btn_tan=Button(root,text="TAN",font=("Ariel",12,"bold"), bg="lightblue",height=2, width=6, command = btnTAN)
btn_tan.grid(row=5,column=2)
btn_log=Button(root,text="LOG",font=("Ariel",12,"bold"), bg="lightblue",height=2, width=6, command = btnLOG)
btn_log.grid(row=5,column=3)


root.mainloop()
