from tkinter import *
import math
from tkinter import messagebox
root = Tk()

# Colors
white = '#FDFEFE'
black = '#000000'
grey = '#CACFD2'
red = '#A93226'
grey_active = '#566573'

dark_grey = '#141414'
med_grey = '#212121'
cus_red = '#c41212'

root.title('KEVIN Scientific Calculator')
root.iconbitmap('calculator.ico')
root.geometry("281x285+550+90")
root.resizable(0, 0)

calc_frame = Frame(root).grid()

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstNum = display1.get()
        secondNum = str(num)
        if self.input_value:
            self.current = secondNum
            self.input_value = False
        else:
            if secondNum == '.':
                if secondNum in firstNum:
                    return
            self.current = firstNum + secondNum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(display1.get())

    def display(self, value):
        display1.delete(0, END)
        display1.insert(0, value)

    def valid_function(self):
        if self.op == "+":
            self.total += self.current
        if self.op == "-":
            self.total -= self.current
        if self.op == "x":
            self.total *= self.current
        if self.op == "÷":
            self.total /= self.current
        if self.op == "%":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    # ============ Standard ============ #
    def DEL(self):
        self.result = False
        self.current = self.current[:-1]
        if self.current == 0:
            self.current = 0
        self.display(self.current)

    def CLS(self):
        self.result = False
        self.current = 0
        self.display(self.current)
        self.input_value = True
        self.total = 0

    def sqrt(self):
        self.result = False
        self.current = math.sqrt(float(display1.get()))
        self.display(self.current)

    def PM(self):
        self.result = False
        self.current = -(float(display1.get()))
        self.display(self.current)

    # ============ Scientific ============ #
    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(display1.get())))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(display1.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(display1.get())))
        self.display(self.current)

    def tau(self):      # 2π
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(display1.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(display1.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(display1.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(display1.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(display1.get()))
        self.display(self.current)

    def mod(self):
        self.result = False
        self.current = math.modf(float(display1.get()))
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(display1.get()))
        self.display(self.current)

    def deg(self):
        self.result = False
        self.current = math.degrees(float(display1.get()))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(math.radians(float(display1.get())))
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(math.radians(float(display1.get())))
        self.display(self.current)

    def acos(self):
        self.result = False
        self.current = math.acosh(math.radians(float(display1.get())))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(display1.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(display1.get()))
        self.display(self.current)

    def expm1(self):
        self.result = False
        self.current = math.expm1(float(display1.get()))
        self.display(self.current)

    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(display1.get()))
        self.display(self.current)

app = Calc()

display1 = Entry(calc_frame, font=("Cambria", 20), bg=white, fg=black, bd=5, width=18, justify=RIGHT)
display1.grid(row=0, column=0, columnspan=4, pady=1)
display1.insert(0, "0")

numberpad = '789456123'
i = 0
btn = []
for row in range(2,5):
    for col in range(3):
        btn.append(Button(calc_frame, width=6, height=1, bg=white, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, text=numberpad[i]))
        btn[i].grid(row=row, column=col, pady=1)
        btn[i]["command"] = lambda n = numberpad[i]: app.numberEnter(n)
        i += 1

# =================== Frame 1 =================== #
DELButton = Button(calc_frame, text="DEL", width=6, height=1, bg=grey, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=app.DEL).grid(row=1, column=0, pady=1)
CLSButton = Button(calc_frame, text="CLS", width=6, height=1, bg=grey, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=app.CLS).grid(row=1, column=1, pady=1)
SqrtButton = Button(calc_frame, text="√", width=6, height=1, bg=grey, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=app.sqrt).grid(row=1, column=2, pady=1)
PlusButton = Button(calc_frame, text="+", width=6, height=1, bg=grey, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=lambda: app.operation("+")).grid(row=1, column=3, pady=1)

MinusButton = Button(calc_frame, text="-", width=6, height=1, bg=grey, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=lambda: app.operation("-")).grid(row=2, column=3, pady=1)
MultiButton = Button(calc_frame, text="×", width=6, height=1, bg=grey, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=lambda: app.operation("x")).grid(row=3, column=3, pady=1)
DivButton = Button(calc_frame, text="÷", width=6, height=1, bg=grey, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=lambda: app.operation("÷")).grid(row=4, column=3, pady=1)

ModuloButton = Button(calc_frame, text="%", width=6, height=1, bg=grey, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=lambda: app.operation("%")).grid(row=5, column=0, pady=1)
ZeroButton = Button(calc_frame, text="0", width=6, height=1, bg=white, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=lambda: app.numberEnter(0)).grid(row=5, column=1, pady=1)
PMButton = Button(calc_frame, text="±", width=6, height=1, bg=grey, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=app.PM).grid(row=5, column=2, pady=1)
EqualButton = Button(calc_frame, text="=", width=6, height=1, bg=red, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=app.sum_of_total).grid(row=5, column=3, pady=1)

# =================== Frame 2 =================== #
PiButton = Button(calc_frame, text="π", width=6, height=1, bg=grey, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=app.pi).grid(row=1, column=4, pady=1)
sinButton = Button(calc_frame, text="sin", width=6, height=1, bg=grey, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=app.sin).grid(row=1, column=5, pady=1)
cosButton = Button(calc_frame, text="cos", width=6, height=1, bg=grey, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=app.cos).grid(row=1, column=6, pady=1)
tanButton = Button(calc_frame, text="tan", width=6, height=1, bg=grey, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=app.tan).grid(row=1, column=7, pady=1)

TwoPiButton = Button(calc_frame, text="2π", width=6, height=1, bg=grey, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=app.tau).grid(row=2, column=4, pady=1)
sinhButton = Button(calc_frame, text="sinh", width=6, height=1, bg=white, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=app.sinh).grid(row=2, column=5, pady=1)
coshButton = Button(calc_frame, text="cosh", width=6, height=1, bg=white, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=app.cosh).grid(row=2, column=6, pady=1)
tanhButton = Button(calc_frame, text="tanh", width=6, height=1, bg=white, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=app.tanh).grid(row=2, column=7, pady=1)

logButton = Button(calc_frame, text="log", width=6, height=1, bg=grey, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=app.log).grid(row=3, column=4, pady=1)
ExpButton = Button(calc_frame, text="Exp", width=6, height=1, bg=white, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=app.exp).grid(row=3, column=5, pady=1)
modButton = Button(calc_frame, text="Mod", width=6, height=1, bg=white, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=app.mod).grid(row=3, column=6, pady=1)
eButton = Button(calc_frame, text="e", width=6, height=1, bg=white, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=app.e).grid(row=3, column=7, pady=1)

log2Button = Button(calc_frame, text="log2", width=6, height=1, bg=grey, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=app.log2).grid(row=4, column=4, pady=1)
degButton = Button(calc_frame, text="deg", width=6, height=1, bg=white, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=app.deg).grid(row=4, column=5, pady=1)
asinhButton = Button(calc_frame, text="asinh", width=6, height=1, bg=white, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=app.asinh).grid(row=4, column=6, pady=1)
acoshButton = Button(calc_frame, text="acosh", width=6, height=1, bg=white, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=app.acosh).grid(row=4, column=7, pady=1)

log10Button = Button(calc_frame, text="log10", width=6, height=1, bg=red, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=app.log10).grid(row=5, column=4, pady=1)
log1pButton = Button(calc_frame, text="log1p", width=6, height=1, bg=grey, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=app.log1p).grid(row=5, column=5, pady=1)
expm1Button = Button(calc_frame, text="expm1", width=6, height=1, bg=white, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=app.expm1).grid(row=5, column=6, pady=1)
lgammaButton = Button(calc_frame, text="lgamma", width=6, height=1, bg=grey, fg=black, activebackground=grey_active, relief=RAISED, font=("calibri", 15), bd=2, command=app.lgamma).grid(row=5, column=7, pady=1)

display2 = Label(calc_frame, text="Scientific Calculator", font=("Cambria", 20), bg=white, fg=black, bd=5, width=18, justify=CENTER).grid(row=0, column=4, columnspan=4)

# =================== Menu =================== #
def exit():
    ask = messagebox.askyesno("Scientific Calculator", "Are you sure?")
    if ask > 0:
        root.destroy()
        return
    else:
        return

def scientific():
    root.resizable(0, 0)
    root.geometry("563x265+350+90")

def standard():
    root.resizable(0, 0)
    root.geometry("281x265+550+90")

# =================== Menu Bar =================== #
menubar = Menu(calc_frame)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Scientific Calculator", command=scientific)
filemenu.add_command(label="Standard Calculator", command=standard)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_separator()
editmenu.add_command(label="Paste")

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
editmenu.add_command(label="View Help")

root.configure(menu=menubar)

root.mainloop()