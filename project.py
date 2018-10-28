from tkinter import *
import os
import sqlite3

cred = 'tempfile.txt'


def signUp():
    global p2
    global n2
    global roots
    roots = Tk()
    roots['bg'] = 'grey'
    roots.title('signUp')
    intro = Label(roots, text='Please Enter new Credidentials\n',background='black',fg='white')
    intro.grid(row=0, column=0, sticky=E)

    n1 = Label(roots, text='New Username: ')
    p1 = Label(roots, text="New Password: ")
    n1.grid(row=1, column=0, sticky=W)
    p1.grid(row=2, column=0, sticky=W)

    n2 = Entry(roots)
    p2 = Entry(roots, show='*')
    n2.grid(row=1, column=1)
    p2.grid(row=2, column=1)

    signButton = Button(roots, text='SignUp', command=FsignUp)
    signButton.grid(columnspan=2, sticky=W)
    roots.mainloop()


def FsignUp():
    with open(cred, 'w') as f:
        f.write(n2.get())
        f.write('\n')
        f.write(p2.get())
        f.close
    roots.destroy()
    login()

def login():
    global n12
    global p12
    global rootA
    rootA = Tk()
    rootA['bg'] = 'grey'
    rootA.title('login')

    instruction = Label(rootA, text="Please login\n",background='black',fg='white')
    instruction.grid(sticky=E)

    namel = Label(rootA, text="UserName: ",background='black',fg='white')
    namep = Label(rootA, text="password: ",background='black',fg='white')
    namel.grid(row=1, sticky=W)
    namep.grid(row=2, sticky=W)

    n12 = Entry(rootA)
    p12 = Entry(rootA, show='*')
    n12.grid(row=1, column=1)
    p12.grid(row=2, column=1)

    loginB = Button(rootA, text='Login',background='black',fg='white', command=checklogin)
    loginB.grid(columnspan=2, sticky=W)

    rmuser = Button(rootA, text="Delete User", fg='red', command=DelUser)
    rmuser.grid(columnspan=2, sticky=W)
    rootA.mainloop()

def generate_command():
    win = Tk()
    win.geometry("850x700")
    win['bg'] = 'grey'
    l = Label(win, text="Report", bg='black', fg='red', width=20)
    l.grid(row=0)

    l1 = Label(win, text="BMI(Body Mass Index): ", background='black', fg='white', width=20)
    l1.grid(row=4, column=2, pady=20)
    e1 = Entry(win, width=20, bd=5)
    e1.grid(row=4, column=3, padx=10)

    l2 = Label(win, text="Weight: ", background='black', fg='white', width=25)
    l2.grid(row=7, column=2, pady=2)
    e2 = Entry(win, width=15, bd=5)
    e2.grid(row=7, column=3)

    l3 = Label(win, text="BP (high/Medium/low): ", background='black', fg='white', width=25)
    l3.grid(row=8, column=2, pady=2)
    e3 = Entry(win, width=15, bd=5)
    e3.grid(row=8, column=3)

    l4 = Label(win, text="Pulse Rate (High,Medium,Low): ", background='black', fg='white', width=25)
    l4.grid(row=9, column=2, pady=2)
    e4 = Entry(win, width=15, bd=5)
    e4.grid(row=9, column=3)

    l4 = Label(win, text="RBC Count (High,Medium,Low): ", background='black', fg='white', width=25)
    l4.grid(row=10, column=2, pady=2)
    e4 = Entry(win, width=15, bd=5)
    e4.grid(row=10, column=3)

    l4 = Label(win, text="WBC Count (High,Medium,Low): ", background='black', fg='white', width=25)
    l4.grid(row=11, column=2, pady=2)
    e4 = Entry(win, width=15, bd=5)
    e4.grid(row=11, column=3)

    l4 = Label(win, text="Platelets (High,Medium,Low): ", background='black', fg='white', width=25)
    l4.grid(row=12, column=2, pady=2)
    e4 = Entry(win, width=15, bd=5)
    e4.grid(row=12, column=3)

    l5 = Label(win, text="HB (High,Medium,Low): ", background='black', fg='white', width=25)
    l5.grid(row=13, column=2, pady=2)
    e5 = Entry(win, width=15, bd=5)
    e5.grid(row=13, column=3)

    l6 = Label(win, text="Uric Acid (High,Medium,low): ", background='black', fg='white', width=25)
    l6.grid(row=14, column=2, pady=2)
    e6 = Entry(win, width=15, bd=5)
    e6.grid(row=14, column=3)

    l7 = Label(win, text="Cholesterol (High,Medium,low): ", background='black', fg='white', width=25)
    l7.grid(row=15, column=2, pady=2)
    e7 = Entry(win, width=15, bd=5)
    e7.grid(row=15, column=3)

    Button(win, text='Exit', bg='red', fg="white", command=win.destroy).place(x=795, y=30)

    win.mainloop()

def save_call():

    print("ccuts")

def proj():
    r.destroy()
    rootA.destroy()
    print("GUI starts fitness calculator")
    top = Tk()
    top.geometry("850x700")
    l = Label(top, text="Fitness Calculator", bg='black', fg='red', width=20)
    l.grid(row=0)
    top['bg'] = 'grey'
    l11 = Label(top, text="Name: ", background='black', fg='white', width=7, font='20px')
    l11.grid(row=4, column=0, pady=20)
    e11 = Entry(top, width=20)
    e11.grid(row=4, column=1, padx=10)


    l12 = Label(top, text="Age: ", background='black', fg='white', width=7)
    l12.grid(row=4, column=2, padx=20)
    e12 = Entry(top, width=6, )
    e12.grid(row=4, column=3)

    l21 = Label(top, text="Gender: ", background='black', fg='white', width=7)
    l21.grid(row=6, column=0, pady=20)
    var = IntVar()
    r1 = Radiobutton(top, text="Female", value=1, variable=var, width=10)
    r2 = Radiobutton(top, text="Male", value=2, variable=var, width=10)
    r1.grid(row=6, column=1)
    r2.grid(row=6, column=2)

    l31 = Label(top, text="Weight: ", background='black', fg='white', width=10)
    l31.grid(row=7, column=0, pady=2)
    e31 = Entry(top, width=15)
    e31.grid(row=7, column=1)

    l41 = Label(top, text="Height: ", background='black', fg='white', width=10)
    l41.grid(row=8, column=0, pady=2)
    e41 = Entry(top, width=15)
    e41.grid(row=8, column=1)

    l51 = Label(top, text="BP Low: ", background='black', fg='white', width=10)
    l51.grid(row=9, column=0, pady=2)
    e51 = Entry(top, width=15)
    e51.grid(row=9, column=1)

    l61 = Label(top, text="BP High: ", background='black', fg='white', width=10)
    l61.grid(row=10, column=0, pady=2)
    e61 = Entry(top, width=15)
    e61.grid(row=10, column=1)

    l71 = Label(top, text="Pulse Rate: ", background='black', fg='white', width=10)
    l71.grid(row=11, column=0, pady=2)
    e71 = Entry(top, width=15)
    e71.grid(row=11, column=1)

    l81 = Label(top, text="RBC Count: ", background='black', fg='white', width=10)
    l81.grid(row=12, column=0, pady=2)
    e81 = Entry(top, width=15)
    e81.grid(row=12, column=1)

    l91 = Label(top, text="WBC Count: ", background='black', fg='white', width=10)
    l91.grid(row=13, column=0, pady=2)
    e91 = Entry(top, width=15)
    e91.grid(row=13, column=1)

    l101= Label(top, text="Platelets: ", background='black', fg='white', width=10)
    l101.grid(row=14, column=0, pady=2)
    e101 = Entry(top, width=15)
    e101.grid(row=14, column=1)

    l201 = Label(top, text="HB: ", background='black', fg='white', width=10)
    l201.grid(row=15, column=0, pady=2)
    e201 = Entry(top, width=15)
    e201.grid(row=15, column=1)

    l301 = Label(top, text="Uric Acid: ", background='black', fg='white', width=10)
    l301.grid(row=16, column=0, pady=2)
    e301 = Entry(top, width=15)
    e301.grid(row=16, column=1)

    l401 = Label(top, text="Cholesterol: ", background='black', fg='white', width=10)
    l401.grid(row=17, column=0, pady=2)
    e401 = Entry(top, width=15)
    e401.grid(row=17, column=1)

    b = Button(top, text="Generate Report", bg="red", fg='white', bd=2, width=20, command=generate_command)
    b.grid(row=19, columnspan=2, pady=40)

    b1 = Button(top, text="Save Info", bg="black", fg='white', bd=2, width=20, command=save_call)
    b1.grid(row=19, column=4, pady=40)

    Button(top, text='Exit', bg='red', fg="white", command=top.destroy).grid(row=1, column=5)
    top.mainloop()


def checklogin():
    global r
    with open(cred) as f:
        data = f.readlines()
        uname = data[0].rstrip()
        pword = data[1].rstrip()
    if n12.get() == uname and p12.get() == pword:
        r = Tk()
        r.title(':D')
        r.geometry('150x150')
        rl = Label(r, text='\n[!] Logged In')
        rl.pack()
        proj()
        r.mainloop()

    else:
        r = Tk()
        r.title(':D')
        r.geometry('150x150')
        rl = Label(r, text='\n[!] Invalid Login')
        rl.pack()
        r.mainloop()


def DelUser():
    os.remove(cred)
    rootA.destroy()
    signUp()


if os.path.isfile(cred):
    login()
else:
    signUp()

