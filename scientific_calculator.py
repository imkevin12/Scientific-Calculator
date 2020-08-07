from tkinter import *
import math
from tkinter import messagebox
root = Tk()

# Colors
dark_grey = '#141414'
med_grey = '#212121'
cus_red = '#c41212'

root.title('KEVIN Scientific Calculator')
root.configure(bg=dark_grey)
root.iconbitmap('calculator.ico')
root.geometry("480x585+0+0")
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
        if self.current==0:
            self.current=0
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

added_value = Calc()

display1 = Entry(calc_frame, font=("arial", 20, "bold"), fg="white", bg=med_grey, bd=30, width=28, justify=RIGHT)
display1.grid(row=0, column=0, columnspan=4, pady=1)
display1.insert(0, "0")

numberpad = '789456123'
i = 0
btn = []
for row in range(2,5):
    for col in range(3):
        btn.append(Button(calc_frame, widt=6, height=2, font=("arial", 20, "bold"), bd=4, text=numberpad[i]))
        btn[i].grid(row=row, column=col, pady=1)
        btn[i]["command"] = lambda n = numberpad[i]: added_value.numberEnter(n)
        i += 1
# =================== Frame 1 =================== #
DELButton = Button(calc_frame, text="DEL", widt=6, height=2, fg="white", font=("arial", 20, "bold"), command=added_value.DEL, bd=4, bg=dark_grey).grid(row=1, column=0, pady=1)
CLSButton = Button(calc_frame, text="CLS", widt=6, height=2, fg="white", font=("arial", 20, "bold"), command=added_value.CLS, bd=4, bg=dark_grey).grid(row=1, column=1, pady=1)
SqrtButton = Button(calc_frame, text="√", widt=6, height=2, fg="white", font=("arial", 20, "bold"), command=added_value.sqrt, bd=4, bg=dark_grey).grid(row=1, column=2, pady=1)
PlusButton = Button(calc_frame, text="+", widt=6, height=2, fg="white", font=("arial", 20, "bold"), command=lambda: added_value.operation("+"), bd=4, bg=dark_grey).grid(row=1, column=3, pady=1)

MinusButton = Button(calc_frame, text="-", widt=6, height=2, fg="white", font=("arial", 20, "bold"), command=lambda: added_value.operation("-"), bd=4, bg=dark_grey).grid(row=2, column=3, pady=1)
MultiButton = Button(calc_frame, text="×", widt=6, height=2, fg="white", font=("arial", 20, "bold"), command=lambda: added_value.operation("x"), bd=4, bg=dark_grey).grid(row=3, column=3, pady=1)
DivButton = Button(calc_frame, text="÷", widt=6, height=2, fg="white", font=("arial", 20, "bold"), command=lambda: added_value.operation("÷"), bd=4, bg=dark_grey).grid(row=4, column=3, pady=1)

DotButton = Button(calc_frame, text="%", widt=6, height=2, fg="white", font=("arial", 20, "bold"), command=lambda: added_value.operation("%"), bd=4, bg=dark_grey).grid(row=5, column=0, pady=1)
ZeroButton = Button(calc_frame, text="0", widt=6, height=2, font=("arial", 20, "bold"), bd=4, command=lambda: added_value.numberEnter(0)).grid(row=5, column=1, pady=1)
PMButton = Button(calc_frame, text="±", widt=6, height=2, fg="white", font=("arial", 20, "bold"), command=added_value.PM, bd=4, bg=dark_grey).grid(row=5, column=2, pady=1)
EqualButton = Button(calc_frame, text="=", widt=6, height=2, fg="white", font=("arial", 20, "bold"), command=added_value.sum_of_total, bd=4, bg=cus_red).grid(row=5, column=3, pady=1)

# =================== Frame 2 =================== #
PiButton = Button(calc_frame, text="π", widt=6, height=2, fg="white", font=("arial", 20, "bold"), command=added_value.pi, bd=4, bg=dark_grey).grid(row=1, column=4, pady=1)
sinButton = Button(calc_frame, text="sin", widt=6, height=2, fg="white", font=("arial", 20, "bold"), command=added_value.sin, bd=4, bg=dark_grey).grid(row=1, column=5, pady=1)
cosButton = Button(calc_frame, text="cos", widt=6, height=2, fg="white", font=("arial", 20, "bold"), command=added_value.cos, bd=4, bg=dark_grey).grid(row=1, column=6, pady=1)
tanButton = Button(calc_frame, text="tan", widt=6, height=2, fg="white", font=("arial", 20, "bold"), command=added_value.tan, bd=4, bg=dark_grey).grid(row=1, column=7, pady=1)

TwoPiButton = Button(calc_frame, text="2π", widt=6, height=2, fg="white", font=("arial", 20, "bold"), command=added_value.tau, bd=4, bg=dark_grey).grid(row=2, column=4, pady=1)
sinhButton = Button(calc_frame, text="sinh", widt=6, height=2, font=("arial", 20, "bold"), command=added_value.sinh, bd=4).grid(row=2, column=5, pady=1)
coshButton = Button(calc_frame, text="cosh", widt=6, height=2, font=("arial", 20, "bold"), command=added_value.cosh, bd=4).grid(row=2, column=6, pady=1)
tanhButton = Button(calc_frame, text="tanh", widt=6, height=2, font=("arial", 20, "bold"), command=added_value.tanh, bd=4).grid(row=2, column=7, pady=1)

logButton = Button(calc_frame, text="log", widt=6, height=2, fg="white", font=("arial", 20, "bold"), command=added_value.log, bd=4, bg=dark_grey).grid(row=3, column=4, pady=1)
ExpButton = Button(calc_frame, text="Exp", widt=6, height=2, font=("arial", 20, "bold"), command=added_value.exp, bd=4).grid(row=3, column=5, pady=1)
modButton = Button(calc_frame, text="Mod", widt=6, height=2, font=("arial", 20, "bold"), command=added_value.mod, bd=4).grid(row=3, column=6, pady=1)
eButton = Button(calc_frame, text="e", widt=6, height=2, font=("arial", 20, "bold"), command=added_value.e, bd=4).grid(row=3, column=7, pady=1)

log2Button = Button(calc_frame, text="log2", widt=6, height=2, fg="white", font=("arial", 20, "bold"), command=added_value.log2, bd=4, bg=dark_grey).grid(row=4, column=4, pady=1)
degButton = Button(calc_frame, text="deg", widt=6, height=2, font=("arial", 20, "bold"), command=added_value.deg, bd=4).grid(row=4, column=5, pady=1)
asinhButton = Button(calc_frame, text="asinh", widt=6, height=2, font=("arial", 20, "bold"), command=added_value.asinh, bd=4).grid(row=4, column=6, pady=1)
acoshButton = Button(calc_frame, text="acosh", widt=6, height=2, font=("arial", 20, "bold"), command=added_value.acosh, bd=4).grid(row=4, column=7, pady=1)

log10Button = Button(calc_frame, text="log10", widt=6, height=2, fg="white", font=("arial", 20, "bold"), command=added_value.log10, bd=4, bg=cus_red).grid(row=5, column=4, pady=1)
log1pButton = Button(calc_frame, text="log1p", widt=6, height=2, fg="white", font=("arial", 20, "bold"), command=added_value.log1p, bd=4, bg=dark_grey).grid(row=5, column=5, pady=1)
expm1Button = Button(calc_frame, text="expm1", widt=6, height=2, font=("arial", 20, "bold"), command=added_value.expm1, bd=4).grid(row=5, column=6, pady=1)
lgammaButton = Button(calc_frame, text="lgamma", widt=6, height=2, fg="white", font=("arial", 20, "bold"), command=added_value.lgamma, bd=4, bg=dark_grey).grid(row=5, column=7, pady=1)

display2 = Label(calc_frame, text="Scientific Calculator", bg=dark_grey, fg="white", font=("arial", 30, "bold"), justify=CENTER).grid(row=0, column=4, columnspan=4)

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
    root.geometry("946x565+0+0")

def standard():
    root.resizable(0, 0)
    root.geometry("480x565+0+0")

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
