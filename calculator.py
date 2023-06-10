from tkinter import Tk, Entry, Button, StringVar

root = Tk()


class Calculator:
    def __init__(self, master):
        master.title('Калькулятор с магией')
        master.geometry('357x420+0+0')
        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=17, font=('Courier', 28), text=self.equation).place(x=0, y=0)

        # Button(width=11,height=4,text='(',relief='flat', bg='pink', command=lambda :self.show('(')).place(x= 0, y = 50)

        Button(width=11, height=4, text='(',
               relief='groove', font=('Courier', 8),borderwidth=2,activebackground='#f754ea', bg='#e5c2dd',
               command=lambda: self.show('(')).place(x=90, y=50)
        Button(width=11, height=4, text=')',
               relief='groove', font=('Courier', 8),borderwidth=2,activebackground='#f754ea', bg='#e5c2dd',
               command=lambda: self.show(')')).place(x=180, y=50)
        Button(width=11, height=4, text='1',
               relief='groove', font=('Courier', 8),borderwidth=2,activebackground='#f754ea', bg='#e5c2dd',
               command=lambda: self.show(1)).place(x=0, y=125)
        Button(width=11, height=4, text='2',
               relief='groove', font=('Courier', 8),borderwidth=2,activebackground='#f754ea', bg='#e5c2dd',
               command=lambda: self.show(2)).place(x=90, y=125)
        Button(width=11, height=4, text='3',
               relief='groove', font=('Courier', 8),borderwidth=2,activebackground='#f754ea', bg='#e5c2dd',
               command=lambda: self.show(3)).place(x=180, y=125)
        Button(width=11, height=4, text='4',
               relief='groove', font=('Courier', 8),borderwidth=2,activebackground='#f754ea', bg='#e5c2dd',
               command=lambda: self.show(4)).place(x=0, y=200)
        Button(width=11, height=4, text='5',
               relief='groove', font=('Courier', 8),borderwidth=2,activebackground='#f754ea', bg='#e5c2dd',
               command=lambda: self.show(5)).place(x=90, y=200)
        Button(width=11, height=4, text='6',
               relief='groove', font=('Courier', 8),borderwidth=2,activebackground='#f754ea', bg='#e5c2dd',
               command=lambda: self.show(6)).place(x=180, y=200)
        Button(width=11, height=4, text='7',
               relief='groove', font=('Courier', 8),borderwidth=2,activebackground='#f754ea', bg='#e5c2dd',
               command=lambda: self.show(7)).place(x=0, y=275)
        Button(width=11, height=4, text='8',
               relief='groove', font=('Courier', 8),borderwidth=2,activebackground='#f754ea', bg='#e5c2dd',
               command=lambda: self.show(8)).place(x=180, y=275)
        Button(width=11, height=4, text='9',
               relief='groove', font=('Courier', 8),borderwidth=2,activebackground='#f754ea', bg='#e5c2dd',
               command=lambda: self.show(9)).place(x=90, y=275)
        Button(width=11, height=4, text='0',
               relief='groove', font=('Courier', 8),borderwidth=2,activebackground='#f754ea', bg='#e5c2dd',
               command=lambda: self.show(0)).place(x=90, y=350)
        Button(width=11, height=4, text='.',
               relief='groove', font=('Courier', 8),borderwidth=2,activebackground='#b1dcfc', bg='#b1dcfc',
               command=lambda: self.show('.')).place(x=0, y=350)
        Button(width=11, height=4, text='+',
               relief='groove', font=('Courier', 8),borderwidth=2,activebackground='#b1dcfc', bg='#b1dcfc',
               command=lambda: self.show('+')).place(x=270, y=275)
        Button(width=11, height=4, text='-',
               relief='groove', font=('Courier', 8),borderwidth=2,activebackground='#b1dcfc', bg='#b1dcfc',
               command=lambda: self.show('-')).place(x=270, y=200)
        Button(width=11, height=4, text='/',
               relief='groove', font=('Courier', 8),borderwidth=2,activebackground='#b1dcfc', bg='#b1dcfc',
               command=lambda: self.show('/')).place(x=270, y=50)
        Button(width=11, height=4, text='x',
               relief='groove', font=('Courier', 8),borderwidth=2,activebackground='#b1dcfc', bg='#b1dcfc',
               command=lambda: self.show('*')).place(x=270, y=125)

        Button(width=11, height=4, text='=',
               relief='groove', font=('Courier', 8),borderwidth=2,activebackground='#7ff5ca', bg='#7ff5ca',
               command=self.solve).place(x=180, y=350, width=177, height=66)

        Button(width=11, height=4, text='C',
               relief='groove', font=('Courier', 8),borderwidth=2,activebackground='#7ff5ca', bg='#7ff5ca',
               command=self.clear).place(x=0, y=50)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except:
            self.equation.set('MAgic')


calculator = Calculator(root)
root.mainloop()
