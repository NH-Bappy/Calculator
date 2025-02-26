from tkinter import *

def button_prees(num):
    
    global equation_text

    if equation_text and equation_text[-1] in ['+', '-', '*', '/'] and num in ['+', '-', '*', '/']:
        return

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)


def equals():
    global equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text =total

    except ZeroDivisionError:

        equation_label.set("error")

        equation_text = ""

    except SyntaxError:

        equation_label.set("syntax error")

        equation_text = ""

def percent():
    global equation_text
    try:
        equation_text = str(eval(equation_text) / 100)
        equation_label.set(equation_text)
    except:
        equation_label.set("error")
        equation_text = ""

def backspace():
    global equation_text
    equation_text = equation_text[:-1]  # Remove last character
    equation_label.set(equation_text)
    

def clear():
    global equation_text 

    equation_label.set("")

    equation_text = ""

Window = Tk() #use for graphical user inter face
Window.title = "Calculator"
Window.geometry("500x500")

equation_text = ""

equation_label = StringVar()

label = Label(Window, textvariable=equation_label,font=('consolas',20),bg="white",width=24,height=2)
label.pack()

frame = Frame(Window)
frame.pack()


button1 = Button(frame, text=1,height=4,width=9,font=35,
                    command= lambda: button_prees(1))
button1.grid(row=0,column=0)

button2 = Button(frame, text=2,height=4,width=9,font=35,
                command=lambda: button_prees(2))
button2.grid(row=0,column=1)

button3 = Button(frame, text=3,height=4,width=9,font=35,
                command=lambda:button_prees(3))
button3.grid(row=0,column=2)

button4 = Button(frame, text=4,height=4,width=9,font=35,
                command=lambda:button_prees(4))
button4.grid(row=1,column=0)

button5 = Button(frame,text=5,height=4,width=9,font=35,
                command=lambda:button_prees(5))
button5.grid(row=1,column=1)

button6 = Button(frame,text=6,height=4,width=9,font=35,
                command=lambda:button_prees(6))
button6.grid(row=1,column=2)

button7 = Button(frame,text=7,height=4,width=9,font=35,
                command=lambda:button_prees(7))
button7.grid(row=2,column=0)

button8 = Button(frame,text=8,height=4,width=9,font=35,
                command=lambda:button_prees(8))
button8.grid(row=2,column=1)

button9 = Button(frame,text=9,height=4,width=9,font=35,
                command=lambda:button_prees(9))
button9.grid(row=2,column=2)

decimal = Button(frame,text='•',height=4,width=9,font=35,
                command=lambda:button_prees('.'))
decimal.grid(row=3,column=0)

button0 = Button(frame,text=0,height=4,width=9,font=35,
                command=lambda:button_prees(0))
button0.grid(row=3,column=1)

equal = Button(frame,text='=',height=4,width=9,font=35,
                command=equals)
equal.grid(row=3,column=2)

plus = Button(frame,text='+',height=4,width=9,font=35,
            command=lambda:button_prees('+'))
plus.grid(row=0,column=4)

minus = Button(frame,text='–',height=4,width=9,font=35,
            command=lambda:button_prees('-'))
minus.grid(row=1,column=4)

multiply = Button(frame,text='×',height=4,width=9,font=35,
            command=lambda:button_prees('*'))
multiply.grid(row=2,column=4)

divide = Button(frame,text='÷',height=4,width=9,font=35,
            command=lambda:button_prees('/'))
divide.grid(row=3,column=4)

clears = Button(frame,text='C',height=4,width=19,font=35,
                command=lambda:clear())
clears.grid(row=4, column=2, columnspan=3)

cancel_button = Button(frame, text='⌫', height=4, width=9, font=35, command=backspace)
cancel_button.grid(row=4, column=0)

percent_button = Button(frame, text='%', height=4, width=9, font=35, command=percent)
percent_button.grid(row=4, column=1)




Window.mainloop() #In Tkinter, mainloop() is used to start and manage the event loop of the GUI application. It keeps the window open and responsive to user interactions (such as clicking buttons, entering text, or closing the window).mainloop() enters an infinite loop that waits for events (mouse clicks, key presses, etc.) and processes them.Without mainloop(), the window will open and immediately close.Listens for and responds to user actions like clicking buttons or resizing the window.


