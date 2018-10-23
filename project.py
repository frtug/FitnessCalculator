from tkinter import *
import tkinter
def proj():
    print("GUI starts fitness calculator")
    top = Tk()
    top.geometry("850x700")
    l = Label(top,text="Fitness Calculator",bg='black',fg='red',width=20)
    l.grid(row=0)
    top["bg"] = "grey"
    
    l1 = Label(top,text="Name: ",background='black',fg='white',width=7)
    l1.grid(row=4,column=0,pady=20)
    e1 = Entry(top,width=20)
    e1.grid(row=4,column=1,padx=10)

    l12 = Label(top,text="Age: ",background='black',fg='white',width=7)
    l12.grid(row =4, column = 2,padx =20)
    e12 = Entry(top,width =6,)
    e12.grid(row=4,column=3)

    l2 = Label(top,text="Gender: ",background='black',fg='white',width=7)
    l2.grid(row=6,column =0,pady=20)
    r1 = Radiobutton(top,text="Male",value=1,variable='var',width=10)
    r2 = Radiobutton(top,text="Female",value=2,variable='var',width=10)
    r1.grid(row=6,column=1)
    r2.grid(row=6,column=2)

    l3 = Label(top,text="Weight: ",background='black',fg='white',width=10)
    l3.grid(row= 7,column =0,pady =2)
    e3 = Entry(top,width=20)
    e3.grid(row=7,column=1)
    
    l3 = Label(top,text="Height: ",background='black',fg='white',width=10)
    l3.grid(row= 8,column =0,pady =2)
    e3 = Entry(top,width=20)
    e3.grid(row=8,column=1)

    l3 = Label(top,text="BP Low: ",background='black',fg='white',width=10)
    l3.grid(row= 9,column =0,pady =2)
    e3 = Entry(top,width=20)
    e3.grid(row=9,column=1)
    
    l3 = Label(top,text="BP High: ",background='black',fg='white',width=10)
    l3.grid(row= 10,column =0,pady =2)
    e3 = Entry(top,width=20)
    e3.grid(row=10,column=1)

    l3 = Label(top,text="Pulse Rate: ",background='black',fg='white',width=10)
    l3.grid(row= 11,column =0,pady =2)
    e3 = Entry(top,width=20)
    e3.grid(row=11,column=1)

    l3 = Label(top,text="RBC Count: ",background='black',fg='white',width=10)
    l3.grid(row= 12,column =0,pady =2)
    e3 = Entry(top,width=20)
    e3.grid(row=12,column=1)

    l3 = Label(top,text="WBC Count: ",background='black',fg='white',width=10)
    l3.grid(row= 13,column =0,pady =2)
    e3 = Entry(top,width=20)
    e3.grid(row=13,column=1)

    l3 = Label(top,text="Platelets: ",background='black',fg='white',width=10)
    l3.grid(row= 14,column =0,pady =2)
    e3 = Entry(top,width=20)
    e3.grid(row=14,column=1)

    l3 = Label(top,text="HB: ",background='black',fg='white',width=10)
    l3.grid(row= 15,column =0,pady =2)
    e3 = Entry(top,width=20)
    e3.grid(row=15,column=1)

    l3 = Label(top,text="Uric Acid: ",background='black',fg='white',width=10)
    l3.grid(row= 16,column =0,pady =2)
    e3 = Entry(top,width=20)
    e3.grid(row=16,column=1)

    l3 = Label(top,text="Cholesterol: ",background='black',fg='white',width=10)
    l3.grid(row= 17,column =0,pady =2)
    e3 = Entry(top,width=20)
    e3.grid(row=17,column=1)


    b = Button(top,text="Generate Report",background="red",bd=2,width=20)
    b.grid(row = 19,columnspan = 2,pady=40)


    b1 = Button(top,text="Save Info",background="black",bd=2,width=20)
    b1.grid(row = 19, column = 4,pady = 40)
    top.mainloop()
proj()
