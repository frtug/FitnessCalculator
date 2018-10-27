from tkinter import *

def generate_command():
    win = Tk()
    win.geometry("850x700")
    win['bg'] = 'grey'
    l = Label(win, text="Report", bg='black', fg='red', width=20)
    l.grid(row=0)

    l1 = Label(win, text="BMI(Body Mass Index): ", background='black', fg='white', width=20, font='20px')
    l1.grid(row=4, column=2, pady=20)
    e1 = Entry(win, width=20,bd=5)
    e1.grid(row=4, column=3, padx=10)

    l3 = Label(win, text="Weight: ", background='black', fg='white', width=25)
    l3.grid(row=7, column=2, pady=2)
    e3 = Entry(win, width=15,bd=5)
    e3.grid(row=7, column=3)

    l3 = Label(win, text="BP (high/Medium/low): ", background='black', fg='white', width=25)
    l3.grid(row=8, column=2, pady=2)
    e3 = Entry(win, width=15,bd=5)
    e3.grid(row=8, column=3)

    l3 = Label(win, text="Pulse Rate (High,Medium,Low): ", background='black', fg='white', width=25)
    l3.grid(row=9, column=2, pady=2)
    e3 = Entry(win, width=15,bd=5)
    e3.grid(row=9, column=3)

    l3 = Label(win, text="RBC Count (High,Medium,Low): ", background='black', fg='white', width=25)
    l3.grid(row=10, column=2, pady=2)
    e3 = Entry(win, width=15,bd=5)
    e3.grid(row=10, column=3)

    l3 = Label(win, text="WBC Count (High,Medium,Low): ", background='black', fg='white', width=25)
    l3.grid(row=11, column=2, pady=2)
    e3 = Entry(win, width=15,bd=5)
    e3.grid(row=11, column=3)

    l3 = Label(win, text="Platelets (High,Medium,Low): ", background='black', fg='white', width=25)
    l3.grid(row=12, column=2, pady=2)
    e3 = Entry(win, width=15,bd=5)
    e3.grid(row=12, column=3)

    l3 = Label(win, text="HB (High,Medium,Low): ", background='black', fg='white', width=25)
    l3.grid(row=13, column=2, pady=2)
    e3 = Entry(win, width=15,bd=5)
    e3.grid(row=13, column=3)

    l3 = Label(win, text="Uric Acid (High,Medium,low): ", background='black', fg='white', width=25)
    l3.grid(row=14, column=2, pady=2)
    e3 = Entry(win, width=15,bd=5)
    e3.grid(row=14, column=3)

    l3 = Label(win, text="Cholesterol (High,Medium,low): ", background='black', fg='white', width=25)
    l3.grid(row=15, column=2, pady=2)
    e3 = Entry(win, width=15,bd=5)
    e3.grid(row=15, column=3)

    Button(win, text='Quit',bg='red',fg="white",command=win.quit).grid(row=1,column=5)


    win.mainloop()

def save_call():
    print('22')

def call_Info():
    print('33')

def proj():

    print("GUI starts fitness calculator")
    top = Tk()
    top.geometry("850x700")
    l = Label(top, text="Fitness Calculator", bg='black', fg='red', width=20)
    l.grid(row=0)

    l1 = Label(top, text="Name: ", background='black', fg='white', width=7, font='20px')
    l1.grid(row=4, column=0, pady=20)
    e1 = Entry(top, width=20)
    e1.grid(row=4, column=1, padx=10)

    l12 = Label(top, text="Age: ", background='black', fg='white', width=7)
    l12.grid(row=4, column=2, padx=20)
    e12 = Entry(top, width=6, )
    e12.grid(row=4, column=3)

    l2 = Label(top, text="Gender: ", background='black', fg='white', width=7)
    l2.grid(row=6, column=0, pady=20)
    var = IntVar()
    r1 = Radiobutton(top, text="Female", value=1, variable=var, width=10)
    r2 = Radiobutton(top, text="Male", value=2, variable=var, width=10)
    r1.grid(row=6, column=1)
    r2.grid(row=6, column=2)

    l3 = Label(top, text="Weight: ", background='black', fg='white', width=10)
    l3.grid(row=7,  column=0, pady=2)
    e3 = Entry(top, width=15)
    e3.grid(row=7,  column=1)

    l3 = Label(top, text="Height: ", background='black', fg='white', width=10)
    l3.grid(row=8 ,  column=0, pady=2)
    e3 = Entry(top, width=15)
    e3.grid(row=8,  column=1)

    l3 = Label(top, text="BP Low: ", background='black', fg='white', width=10)
    l3.grid(row=9,  column=0, pady=2)
    e3 = Entry(top, width=15)
    e3.grid(row=9,  column=1)

    l3 = Label(top, text="BP High: ", background='black', fg='white', width=10)
    l3.grid(row=10, column=0, pady=2)
    e3 = Entry(top, width=15)
    e3.grid(row=10, column=1)

    l3 = Label(top, text="Pulse Rate: ", background='black', fg='white', width=10)
    l3.grid(row=11, column=0, pady=2)
    e3 = Entry(top, width=15)
    e3.grid(row=11, column=1)

    l3 = Label(top, text="RBC Count: ", background='black', fg='white', width=10)
    l3.grid(row=12, column=0, pady=2)
    e3 = Entry(top, width=15)
    e3.grid(row=12, column=1)

    l3 = Label(top, text="WBC Count: ", background='black', fg='white', width=10)
    l3.grid(row=13, column=0, pady=2)
    e3 = Entry(top, width=15)
    e3.grid(row=13, column=1)

    l3 = Label(top, text="Platelets: ", background='black', fg='white', width=10)
    l3.grid(row=14, column=0, pady=2)
    e3 = Entry(top, width=15)
    e3.grid(row=14, column=1)

    l3 = Label(top, text="HB: ", background='black', fg='white', width=10)
    l3.grid(row=15, column=0, pady=2)
    e3 = Entry(top, width=15)
    e3.grid(row=15, column=1)

    l3 = Label(top, text="Uric Acid: ", background='black', fg='white', width=10)
    l3.grid(row=16, column=0, pady=2)
    e3 = Entry(top, width=15)
    e3.grid(row=16, column=1)

    l3 = Label(top, text="Cholesterol: ", background='black', fg='white', width=10)
    l3.grid(row=17, column=0, pady=2)
    e3 = Entry(top, width=15)
    e3.grid(row=17, column=1)

    b = Button(top, text="Generate Report", bg="red",fg='white', bd=2, width=20, command=generate_command)
    b.grid(row=19,  columnspan=2, pady=40)

    b1 = Button(top, text="Save Info", bg="black",fg='white', bd=2, width=20, command=save_call)
    b1.grid(row=19,  column=4, pady=40)

    Button(top, text='Quit',bg='red',fg="white",command=top.quit).grid(row=1,column=5)
    top.mainloop()

proj()
