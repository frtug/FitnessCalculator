from tkinter import *
import os
import sqlite3
from tkinter import messagebox
import time
#......
cred ='passdataa.db'
db1  =sqlite3.connect(cred)
c1 = db1.cursor()
c1.execute("""CREATE TABLE IF NOT EXISTS keys(User_name TEXT NOT NULL,Password TEXT NOT NULL)""")
db1.commit()

#..................... for the login and signUP .......................................
db = sqlite3.connect("data1.db")
c = db.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS User(ID INTEGER PRIMARY KEY,Name TEXT,Age INTEGER,
 Weight INTEGER,Height INTEGER,BP_Low INTEGER,BP_High INTEGER,Pulse_Rate INTEGER,RBC_Count INTEGER,WBC_Count INTEGER,
 Platelets INTEGER,HB INTEGER,Uric_Acid INTEGER,Cholesterol INTEGER)""")

db.commit()


def signUp():
    global p2
    global n2
    global roots
    roots = Tk()
    roots.geometry('500x300')
    roots['bg'] = 'grey'
    roots.title('SignUp')
    intro = Label(roots, text='Please Register', background='black', fg='white', font=("Bold", 40))
    intro.grid(row=0, sticky=N, padx=50, pady=10)

    n1 = Label(roots, text=' Username: ', background='black', fg='white', font=("Cursive", 20))
    p1 = Label(roots, text=" Password: ", background='black', fg='white', font=("Cursive", 20))
    n1.grid(row=1, sticky=W, column=0, padx=20, pady=20)
    p1.grid(row=2, sticky=W, column=0, padx=20, pady=20)

    n2 = Entry(roots)
    p2 = Entry(roots, show='*')
    n2.grid(row=1, column=0, sticky=E, padx=20)
    p2.grid(row=2, column=0, sticky=E, padx=20)

    signButton = Button(roots, text='SignUp', command=FsignUp, background='black', fg='red')
    signButton.grid(column=0, row=3, padx=40, columnspan=1)
    roots.mainloop()

def FsignUp():
    
     username = n2.get()
     password = p2.get()
     if len(username)!=0 and len(password)!=0 :
      c1.execute("INSERT INTO keys VALUES(?,?)",(username,password))
      db1.commit()
      msg = messagebox.showinfo('SignUp','Successfully')

      roots.destroy()
      #msg = messagebox.showinfo('Error','Enter the Values')
      login()
     else:
        msg = messagebox.showinfo('Error','Enter the Credentials')


def generate_command():

  if len(Name_value) != 0 and len(ID_value) != 0 and len(Age_value) != 0 and len(Weight_value) != 0 and len(
           Height_value) != 0 and len(BP_Low_value) != 0 and len(BP_High_value) != 0 and len(
           Pulse_Rate_value) != 0 and len(RBC_Count_value) != 0 and len(WBC_Count_value) != 0 and len(
           Platelets_value) != 0 and len(HB_value) != 0 and len(Uric_Acid_value)!=0 and len(Cholestreol_value) != 0:

    win = Tk()
    win.geometry("850x700")
    win['bg'] = 'grey'
    l = Label(win, text="Report", bg='black', fg='red', width=20)
    l.grid(row=0)


    l01 = Label(win, text="ID : ", background='black', fg='white', width=7)
    l01.grid(row=2, column=0, pady=20)
    e01 = Entry(win, width=20)
    e01.grid(row=2, column=1, padx=10)
    e01.insert(0,str(ID_value))
    e01.config(state = 'disabled')


    l010 = Label(win, text="Name : ", background='black', fg='white', width=7)
    l010.grid(row=3, column=0, pady=20)
    e010 = Entry(win, width=20)
    e010.grid(row=3, column=1, padx=10)
    e010.insert(0,str(Name_value))
    e010.config(state = 'disabled')


    BMI_value = int(Weight_value)/(int(Height_value)*int(Height_value))
    l1 = Label(win, text="BMI(Body Mass Index): ", background='black', fg='white', width=20)
    l1.grid(row=3, column=2, pady=20)
    e1 = Entry(win, width=20, bd=5)
    e1.grid(row=3, column=3, padx=10)
    e1.insert(0,str(BMI_value))
    e1.config(state = 'disabled')


    l2 = Label(win, text="Weight: ", background='black', fg='white', width=25)
    l2.grid(row=4, column=2, pady=2)
    e2 = Entry(win, width=15, bd=5)
    e2.grid(row=4, column=3)
    e2.insert(0,str(Weight_value))
    e2.config(state = 'disabled')


    BP_value = (int(BP_Low_value)+int(BP_High_value))/2
    l3 = Label(win, text="BP (high/Medium/low): ", background='black', fg='white', width=25)
    l3.grid(row=5, column=2, pady=2)
    e3 = Entry(win, width=15, bd=5)
    e3.grid(row=5, column=3)
    e3.insert(0,str(BP_value))
    e3.config(state = 'disabled')



    l4 = Label(win, text="Pulse Rate (High,Medium,Low): ", background='black', fg='white', width=25)
    l4.grid(row=6, column=2, pady=2)
    e4 = Entry(win, width=15, bd=5)
    e4.grid(row=6, column=3)
    e4.insert(0,str(Pulse_Rate_value))
    e4.config(state = 'disabled')


    l5 = Label(win, text="RBC Count (High,Medium,Low): ", background='black', fg='white', width=25)
    l5.grid(row=7, column=2, pady=2)
    e5 = Entry(win, width=15, bd=5)
    e5.grid(row=7, column=3)
    e5.insert(0,str(RBC_Count_value))
    e5.config(state = 'disabled')


    l6 = Label(win, text="WBC Count (High,Medium,Low): ", background='black', fg='white', width=25)
    l6.grid(row=8, column=2, pady=2)
    e6 = Entry(win, width=15, bd=5)
    e6.grid(row=8, column=3)
    e6.insert(0, str(WBC_Count_value))
    e6.config(state = 'disabled')


    l7 = Label(win, text="Platelets (High,Medium,Low): ", background='black', fg='white', width=25)
    l7.grid(row=9, column=2, pady=2)
    e7 = Entry(win, width=15, bd=5)
    e7.grid(row=9, column=3)
    e7.insert(0, str(Platelets_value))
    e7.config(state = 'disabled')



    l8 = Label(win, text="HB (High,Medium,Low): ", background='black', fg='white', width=25)
    l8.grid(row=10, column=2, pady=2)
    e8 = Entry(win, width=15, bd=5)
    e8.grid(row=10, column=3)
    e8.insert(0, str(HB_value))
    e8.config(state = 'disabled')



    l9 = Label(win, text="Uric Acid (High,Medium,low): ", background='black', fg='white', width=25)
    l9.grid(row=11, column=2, pady=2)
    e9 = Entry(win, width=15, bd=5)
    e9.grid(row=11, column=3)
    e9.insert(0, str(Uric_Acid_value))
    e9.config(state = 'disabled')


    l10 = Label(win, text="Cholesterol (High,Medium,low): ", background='black', fg='white', width=25)
    l10.grid(row=12, column=2, pady=2)
    e10 = Entry(win, width=15, bd=5)
    e10.grid(row=12, column=3)
    e10.insert(0, str(Cholestreol_value))
    e10.config(state = 'disabled')

    Button(win, text='Exit', bg='red', fg="white", command=win.destroy).place(x=795, y=30)

    win.mainloop()
  else:
    msg = messagebox.showinfo('Error','Enter the Values')
def save_Info():
  global Name_value
  Name_value = e11.get()
  global ID_value
  ID_value = e00.get()
  global Age_value
  Age_value = e12.get()
  global Weight_value
  Weight_value = e31.get()
  global Height_value
  Height_value = e41.get()
  global BP_Low_value
  BP_Low_value = e51.get()
  global BP_High_value
  BP_High_value = e61.get()
  global Pulse_Rate_value
  Pulse_Rate_value = e71.get()
  global RBC_Count_value
  RBC_Count_value = e81.get()
  global WBC_Count_value
  WBC_Count_value = e91.get()
  global Platelets_value
  Platelets_value = e101.get()
  global HB_value
  HB_value = e201.get()
  global Uric_Acid_value
  Uric_Acid_value = e301.get()
  global Cholestreol_value
  Cholestreol_value = e401.get()

  if len(Name_value)!=0 and len(ID_value)!=0 and len(Age_value)!=0 and len(Weight_value)!=0 and len(Height_value)!=0 and len(BP_Low_value)!=0 and len(BP_High_value)!=0 and len(Pulse_Rate_value)!=0 and len(RBC_Count_value)!=0 and len(WBC_Count_value)!=0 and len(Platelets_value)!=0 and len(HB_value)!=0 and len(Uric_Acid_value)!=0 and len(Cholestreol_value)!=0:

    c.execute("INSERT INTO User VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(ID_value,Name_value,Age_value,
                                                   Weight_value,Height_value,
                                                   BP_Low_value,BP_High_value,
                                                   Pulse_Rate_value,RBC_Count_value,
                                                   WBC_Count_value,Platelets_value,
                                                   HB_value,Uric_Acid_value,Cholestreol_value))
    msg = messagebox.showinfo('Message','Successfull Entered Values')
  else:
    msg = messagebox.showinfo('Message','Not Valid Entry')

  db.commit()
  d = c.execute("SELECT * FROM User")
  print(d.fetchall())
  db.commit()
  c.close()
  
def quitr():
    root.destroy()
    quit()
    
    
def proj():
    global top
    rootA.destroy()
    print("GUI starts fitness calculator")
    top = Tk()
    top.geometry("1200x900")
    l = Label(top, text="Fitness Calculator", bg='black', fg='red', width=20,font=("",40))
    l.grid(row=0,column=1,columnspan=1)
    top['bg'] = 'grey'
    l11 = Label(top, text="Name: ", background='black', fg='white', width=7)
    l11.grid(row=4, column=0, pady=20)
    global e11
    e11= Entry(top, width=20)
    e11.grid(row=4, column=1, padx=10)

    global e00
    l00 = Label(top, text="ID : ", background='black', fg='white', width=7)
    l00.grid(row=3, column=0, pady=20)
    e00 = Entry(top, width=20)
    e00.grid(row=3, column=1, padx=10)

    global e12
    l12 = Label(top, text="Age: ", background='black', fg='white', width=7)
    l12.grid(row=4, column=2, padx=20)
    e12 = Entry(top, width=6, )
    e12.grid(row=4, column=3)

    l21 = Label(top, text="Gender: ", background='black', fg='white', width=7)
    l21.grid(row=6, column=0, pady=20,padx=10)
    var = IntVar()
    r1 = Radiobutton(top, text="Female", value=1, variable=var, width=10)
    r2 = Radiobutton(top, text="Male", value=2, variable=var, width=10)
    r1.grid(row=6, column=1)
    r2.grid(row=6, column=2)

    global e31
    l31 = Label(top, text="Weight: ", background='black', fg='white', width=10)
    l31.grid(row=7, column=0, pady=2,padx=10)
    e31 = Entry(top, width=15)
    e31.grid(row=7, column=1)

    global e41
    l41 = Label(top, text="Height: ", background='black', fg='white', width=10)
    l41.grid(row=8, column=0, pady=2,padx=10)
    e41 = Entry(top, width=15)
    e41.grid(row=8, column=1)

    global e51
    l51 = Label(top, text="BP Low: ", background='black', fg='white', width=10)
    l51.grid(row=9, column=0, pady=2,padx=10)
    e51 = Entry(top, width=15)
    e51.grid(row=9, column=1)

    global e61
    l61 = Label(top, text="BP High: ", background='black', fg='white', width=10)
    l61.grid(row=10, column=0, pady=2,padx=10)
    e61 = Entry(top, width=15)
    e61.grid(row=10, column=1)

    global e71
    l71 = Label(top, text="Pulse Rate: ", background='black', fg='white', width=10)
    l71.grid(row=11, column=0, pady=2,padx=10)
    e71 = Entry(top, width=15)
    e71.grid(row=11, column=1)

    global e81
    l81 = Label(top, text="RBC Count: ", background='black', fg='white', width=10)
    l81.grid(row=12, column=0, pady=2,padx=10)
    e81 = Entry(top, width=15)
    e81.grid(row=12, column=1)

    global e91
    l91 = Label(top, text="WBC Count: ", background='black', fg='white', width=10)
    l91.grid(row=13, column=0, pady=2,padx=10)
    e91 = Entry(top, width=15)
    e91.grid(row=13, column=1)

    global e101
    l101= Label(top, text="Platelets: ", background='black', fg='white', width=10)
    l101.grid(row=14, column=0, pady=2,padx=10)
    e101 = Entry(top, width=15)
    e101.grid(row=14, column=1)

    global e201
    l201 = Label(top, text="HB: ", background='black', fg='white', width=10)
    l201.grid(row=15, column=0, pady=2,padx=10)
    e201 = Entry(top, width=15)
    e201.grid(row=15, column=1)

    global e301
    l301 = Label(top, text="Uric Acid: ", background='black', fg='white', width=10)
    l301.grid(row=16, column=0, pady=2,padx=10)
    e301 = Entry(top, width=15)
    e301.grid(row=16, column=1)

    global e401
    l401 = Label(top, text="Cholesterol: ", background='black', fg='white', width=10)
    l401.grid(row=17, column=0, pady=2,padx=10)
    e401 = Entry(top, width=15)
    e401.grid(row=17, column=1)

    b = Button(top, text="Generate Report", bg="red", fg='white', bd=2, width=20, command=generate_command)
    b.grid(row=19, columnspan=2, pady=40)

    b1 = Button(top, text="Save Info", bg="black", fg='white', bd=2, width=20, command=save_Info)
    b1.grid(row=19, column=4, pady=40)

    Button(top, text='Exit', bg='red', fg="white", command=quitr).grid(row=1, column=5)
    top.mainloop()
    
def checklogin():
    
    global r
    if n12.get() != "" and p12.get() != "":
        print(n12.get(),p12.get())
      #  f = c1.execute("SELECT  User_name FROM keys")
       # print(f.fetchall())
        d1 = c1.execute("SELECT User_name FROM keys WHERE User_name ='{}'".format(n12.get()))
        d2 = d1.fetchone()
        d1 = c1.execute("SELECT Password FROM keys WHERE Password ='{}'".format(p12.get()))
        d3 = d1.fetchone()
        db1.commit()
        print("d2=",d2[0],"d3=",d3[0])
        if n12.get() == d2[0] and p12.get() == d3[0]:
            print("Works in the value")
            proj()
        else:
            print("Error")
            msg = messagebox.showinfo('Error','Password or UserName')

      
    else:
        r = Tk()
        r.title('Unknown')
        r.geometry('300x150')
        rl = Label(r, text='\n[!] Fill the Login Credentionals')
        rl.pack()
        r.mainloop()
    

def login():
    global n12
    global p12
    global rootA
    rootA = Tk()

    rootA['bg'] = 'grey'
    rootA.title('Login')
    rootA.geometry("500x300")
    instruction = Label(rootA, text="Please Login",background='black',fg='white',font=("",30))
    instruction.grid(sticky=N,padx=20,pady=20,columnspan=2)

    namel = Label(rootA, text="UserName: ",background='black',fg='white',font=('',20))
    namep = Label(rootA, text="PassWord: ",background='black',fg='white',font=('',20))
    namel.grid(row=1, sticky=W,pady=10,padx=20)
    namep.grid(row=2, sticky=W,pady=10,padx=20)

    n12 = Entry(rootA)
    p12 = Entry(rootA, show='*')
    n12.grid(row=1, column=1,pady=10,sticky=E)
    p12.grid(row=2, column=1,pady=10,sticky=E)

    loginB = Button(rootA, text='SignUp',background='black',fg='white', command=DeUser)
    loginB.grid(row=3,columnspan=2, sticky=W,pady=10)

    rmuser = Button(rootA, text="login ", fg='red', command=checklogin)
    rmuser.grid(row=3,columnspan=2, sticky=E,pady=10)
    rootA.mainloop()
    c1.close()
    
#needs to be changed


def DeUser():
 #   os.remove(cred)
    rootA.destroy()
    signUp()

if os.path.isfile(cred):
    login()
else:
    signUp()

