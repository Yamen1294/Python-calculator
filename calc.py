import tkinter as tk
from tkinter import *


calco=tk.Tk()
calco.title("Calculater")
calco.geometry('570x600')
calco.resizable(FALSE,FALSE)
calco.config(background='#17161b')
#FUNS
equation = ""

def show(value):
    global equation
    equation += value
    label_result.config(text= equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)
    

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result= eval(equation)
        except:
            result= "Error"
            equation = ""
    label_result.config(text= result)
    
label_result = tk.Label(
    calco,
    width=25,
    height=2,
    text='',
    font=('Arial',30)
)
label_result.pack()   

#bottons
#LINE ('C','/','%','*')
clear_button = tk.Button(
    calco,
    text='C',
    width=5,
    height=1,
    font=('Arial',30,'bold'),
    fg='#fff',
    bg='#3697f5',
    bd=3,
    command=lambda: clear()
)
clear_button.place(x=10,y=117)

divide_button = tk.Button(
    calco,
    text='/',
    width=5,
    height=1,
    font=('Arial',30,'bold'),
    fg='#fff',
    bg='#2a2d36',
    bd=3,
    command=lambda : show('/')
)
divide_button.place(x=150,y=117)

reminder_button = tk.Button(
    calco,
    text='%',
    width=5,
    height=1,
    font=('Arial',30,'bold'),
    fg='#fff',
    bg='#2a2d36',
    bd=3,
    command=lambda : show('%')
)
reminder_button.place(x=290,y=117)

multiplay_button = tk.Button(
    calco,
    text='*',
    width=5,
    height=1,
    font=('Arial',30,'bold'),
    fg='#fff',
    bg='#2a2d36',
    bd=3,
    command=lambda : show('*')
)
multiplay_button.place(x=430,y=117)

#line 7 8 9 -

seven_button = tk.Button(
    calco,
    text='7',
    width=5,
    height=1,
    font=('Arial',30,'bold'),
    fg='#fff',
    bg='#2a2d36',
    bd=3,
    command=lambda : show('7')
)
seven_button.place(x=10,y=217)

eight_button = tk.Button(
    calco,
    text='8',
    width=5,
    height=1,
    font=('Arial',30,'bold'),
    fg='#fff',
    bg='#2a2d36',
    bd=3,
    command=lambda : show('8')
)
eight_button.place(x=150,y=217)

nine_button = tk.Button(
    calco,
    text='9',
    width=5,
    height=1,
    font=('Arial',30,'bold'),
    fg='#fff',
    bg='#2a2d36',
    bd=3,
    command=lambda : show('9')
)
nine_button.place(x=290,y=217)

minues_button = tk.Button(
    calco,
    text='-',
    width=5,
    height=1,
    font=('Arial',30,'bold'),
    fg='#fff',
    bg='#2a2d36',
    bd=3,
    command=lambda : show('-')
)
minues_button.place(x=430,y=217)


#4 5 6 +

four_button = tk.Button(
    calco,
    text='4',
    width=5,
    height=1,
    font=('Arial',30,'bold'),
    fg='#fff',
    bg='#2a2d36',
    bd=3,
    command=lambda : show('4')
)
four_button.place(x=10,y=317)

five_button = tk.Button(
    calco,
    text='5',
    width=5,
    height=1,
    font=('Arial',30,'bold'),
    fg='#fff',
    bg='#2a2d36',
    bd=3,
    command=lambda : show('5')
)
five_button.place(x=150,y=317)

six_button = tk.Button(
    calco,
    text='6',
    width=5,
    height=1,
    font=('Arial',30,'bold'),
    fg='#fff',
    bg='#2a2d36',
    bd=3,
    command=lambda : show('6')
)
six_button.place(x=290,y=317)

plus_button = tk.Button(
    calco,
    text='+',
    width=5,
    height=1,
    font=('Arial',30,'bold'),
    fg='#fff',
    bg='#2a2d36',
    bd=3,
    command=lambda : show('+')
)
plus_button.place(x=430,y=317)
#1 2 3 

one_button = tk.Button(
    calco,
    text='1',
    width=5,
    height=1,
    font=('Arial',30,'bold'),
    fg='#fff',
    bg='#2a2d36',
    bd=3,
    command=lambda : show('1')
)
one_button.place(x=10,y=417)

two_button = tk.Button(
    calco,
    text='2',
    width=5,
    height=1,
    font=('Arial',30,'bold'),
    fg='#fff',
    bg='#2a2d36',
    bd=3,
    command=lambda : show('2')
)
two_button.place(x=150,y=417)

three_button = tk.Button(
    calco,
    text='3',
    width=5,
    height=1,
    font=('Arial',30,'bold'),
    fg='#fff',
    bg='#2a2d36',
    bd=3,
    command=lambda : show('3')
)
three_button.place(x=290,y=417)
# zero
zero_button = tk.Button(
    calco,
    text='0',
    width=11,
    height=1,
    font=('Arial',30,'bold'),
    fg='#fff',
    bg='#2a2d36',
    bd=3,
    command=lambda : show('0')
)
zero_button.place(x=10,y=517)

#line . =

dot_button = tk.Button(
    calco,
    text='.',
    width=5,
    height=1,
    font=('Arial',30,'bold'),
    fg='#fff',
    bg='#2a2d36',
    bd=3,
    command=lambda : show('.')
)
dot_button.place(x=290,y=517)

equal_button = tk.Button(
    calco,
    text='=',
    width=5,
    height=3,
    font=('Arial',30,'bold'),
    fg='#fff',
    bg='#fe9037',
    bd=3,
    command=lambda : calculate()
)
equal_button.place(x=430,y=417)
calco.mainloop()