from tkinter import *
from tkinter import ttk
import math


i = 0
def get_vars(num):
    global i
    text.insert(i, num)
    i+=1

def get_calcs(sym):
    global i
    length = len(sym)
    text.insert(i, sym)
    i+=length

def clear():
    text.delete(0,END)
    
# def sin():
#     txt_input = text.get()
#     if("sin" in txt_input):
#         txt_input = math.sin(txt_input)

def calculate():
    entire_string = text.get()
    try:
        a = str(eval(entire_string))
        clear()
        text.insert(0,a)
    except Exception:
        clear()
        text.insert(0,"Error")
    
#set up box

root = Tk()
root.title("My Calculator in Python")
#root.minsize(width=250, height=250)

#set up frame
mainframe = ttk.Frame(root, padding=(3, 3, 3, 3))
mainframe.grid(column=0, row=0, sticky=(N, W, S, E))

root.columnconfigure(0, weight=1)
root.rowconfigure(0,weight=1)
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
#output/input window
calculation = StringVar()
text = ttk.Entry(mainframe)
text.grid(column=1, row=1, columnspan=6, sticky=(N, W, S, E))


#buttons
btnOne   = ttk.Button(mainframe, command= lambda: get_vars(1),  text="1").grid(column=1, row=5, sticky=(N, W, S, E))
btnTwo   = ttk.Button(mainframe, command= lambda: get_vars(2),  text="2").grid(column=2, row=5, sticky=(N, W, S, E))
btnThree = ttk.Button(mainframe, command= lambda: get_vars(3),  text="3").grid(column=3, row=5, sticky=(N, W, S, E))
btnFour  = ttk.Button(mainframe, command= lambda: get_vars(4),  text="4").grid(column=1, row=4, sticky=(N, W, S, E))
btnFive  = ttk.Button(mainframe, command= lambda: get_vars(5),  text="5").grid(column=2, row=4, sticky=(N, W, S, E))
btnSix   = ttk.Button(mainframe, command= lambda: get_vars(6),  text="6").grid(column=3, row=4, sticky=(N, W, S, E))
btnSeven = ttk.Button(mainframe, command= lambda: get_vars(7),  text="7").grid(column=1, row=3, sticky=(N, W, S, E))
btnEight = ttk.Button(mainframe, command= lambda: get_vars(8),  text="8").grid(column=2, row=3, sticky=(N, W, S, E))
btnNine  = ttk.Button(mainframe, command= lambda: get_vars(9),  text="9").grid(column=3, row=3, sticky=(N, W, S, E))
btnZero  = ttk.Button(mainframe, command= lambda: get_vars(0),  text="0").grid(column=2, row=6, sticky=(N, W, S, E))
btnDot   = ttk.Button(mainframe, command= lambda: get_vars("."),text=".").grid(column=3, row=6, sticky=(N, W, S, E))

#calculation buttons
btnSin   = ttk.Button(mainframe, command= lambda: get_calcs("sin"),text="sin").grid(column=1, row=2, sticky=(N, W, S, E))
btnCos   = ttk.Button(mainframe, command= lambda: get_calcs("cos"),text="cos").grid(column=2, row=2, sticky=(N, W, S, E))
btnTan   = ttk.Button(mainframe, command= lambda: get_calcs("tan"),text="tan").grid(column=3, row=2, sticky=(N, W, S, E))
btnDiv   = ttk.Button(mainframe, command= lambda: get_calcs("/"),  text="/").grid(column=4, row=2, sticky=(N, W, S, E))
btnMult  = ttk.Button(mainframe, command= lambda: get_calcs("*"),  text="*").grid(column=4, row=3, sticky=(N, W, S, E))
btnAdd   = ttk.Button(mainframe, command= lambda: get_calcs("+"),  text="+").grid(column=4, row=4, sticky=(N, W, S, E))
btnSub   = ttk.Button(mainframe, command= lambda: get_calcs("-"),  text="-").grid(column=4, row=5, sticky=(N, W, S, E))
btnEqual = ttk.Button(mainframe, command= lambda: calculate(),     text="=").grid(column=4, row=6, sticky=(N, W, S, E))
btnAC    = ttk.Button(mainframe, command= lambda: clear(),         text="AC").grid(column=1, row=6, sticky=(N, W, S, E))
btnAC    = ttk.Button(mainframe, command= lambda: get_calcs(")"),  text=")").grid(column=5, row=2, sticky=(N, W, S, E))
btnAC    = ttk.Button(mainframe, command= lambda: get_calcs("("),  text="(").grid(column=5, row=3, sticky=(N, W, S, E))

#bind
root.bind("<1>", btnOne)
root.bind("<2>", btnTwo)
root.bind("<3>", btnThree)
root.bind("<4>", btnFour)
root.bind("<5>", btnFive)
root.bind("<6>", btnSix)
root.bind("<7>", btnSeven)
root.bind("<8>", btnEight)
root.bind("<9>", btnNine)
root.bind("<0>", btnZero)
root.bind("<.>", btnDot)
root.bind(math.sin, btnSin)
root.bind(math.cos, btnCos)
root.bind(math.tan, btnTan)
root.bind("</>", btnDiv)
root.bind("<*>", btnMult) 
root.bind("<+>", btnAdd)
root.bind("<->", btnSub)
root.bind("<=>", btnEqual)



root.mainloop()