from tkinter import *
import tkinter.messagebox
import sqlite3
import library
def enter1():
    global eu
    global ep
    global user
    global pwd
    global log
    x=(eu.get(),ep.get())
    conn=sqlite3.connect('libarary.db')
    rows=conn.execute(f"SELECT * FROM LOGIN WHERE USERNAME='{x[0]}' AND PASSWORD='{x[1]}'").fetchall()
    try:
        if rows[0][0]==x[0] and rows[0][1]==str(x[1]):
            library.books(log)
        else:
            tkinter.messagebox.showinfo('error','invalid username')
    except:
        tkinter.messagebox.showinfo('error','invalid username')
    conn.close()
        
def displaybfr(e):
    bfr['bg']='powder blue'
def displaybfr1(e):
    bfr['bg']='gray'
def displaybfl(e):
    bfl['bg']='powder blue'
def displaybfl1(e):
    bfl['bg']='gray'
def enter():
    global eul
    global epl
    global userl
    global pwdl
    global reg
    x=(eul.get(),epl.get())
    print(x)
    a=x[0]
    b=x[1]
    conn=sqlite3.connect('libarary.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS LOGIN
    (USERNAME TEXT PRIMARY KEY, PASSWORD text)''')
    try:
        conn.execute(f"INSERT INTO LOGIN VALUES('{a}','{b}')")
        conn.commit()
    except Exception as e:
        tkinter.messagebox.showinfo('error','invalid username')
        print(e)
        userl.delete(0,END)
        pwdl.delete(0,END)
    finally:
        userl.delete(0,END)
        pwdl.delete(0,END)
        conn.close()
        reg.destroy()
def reg():
    global eul
    global epl
    global userl
    global pwdl
    global reg
    reg=Toplevel(main)
    reg.title('LOGIN')
    reg.config(bg='white')
    lbl21=Label(reg,text='PLEASE FILL DETAILS',bg='white',fg='black',font='arial 20 bold')
    lbl21.pack(padx=10,pady=10)
    lblus=Label(reg,text='USERNAME ',bg='white',fg='black',font='arial 28 bold',width=20)
    lblus.pack(padx=15,pady=15)
    eul=StringVar()
    epl=StringVar() 
    userl=Entry(reg,textvariable=eul,bg='light pink',fg='black',font='arial 28 bold',relief=RAISED,width=20)
    userl.pack(padx=5,pady=5)
    lblps=Label(reg,text='PASSWORD ',bg='white',fg='black',width=20,font='arial 28 bold')
    lblps.pack(padx=15,pady=15)
    pwdl=Entry(reg,textvariable=epl,bg='light pink',fg='black',width=20,font='arial 28 bold',relief=RAISED)
    pwdl.pack(padx=5,pady=5)
    bfe=Button(reg,text='RESISTER',bg='light pink',fg='black',font='arial 30 bold',
               relief=FLAT,command=enter)
    bfe.pack(padx=20,pady=20)
    reg.mainloop()
    
def log():
    global eu
    global ep
    global user
    global pwd
    global log
    log=Toplevel(main)
    log.title('LOGIN')
    log.config(bg='white')
    lbl21=Label(log,text='PLEASE FILL DETAILS',bg='white',fg='black',font='arial 20 bold')
    lbl21.pack(padx=10,pady=10)
    lblus=Label(log,text='USERNAME ',bg='white',fg='black',font='arial 28 bold',width=20)
    lblus.pack(padx=15,pady=15)
    eu=StringVar()
    ep=StringVar()
    user=Entry(log,textvariable=eu,bg='light pink',fg='black',font='arial 28 bold',relief=RAISED,width=20)
    user.pack(padx=5,pady=5)
    lblps=Label(log,text='PASSWORD ',bg='white',fg='black',width=20,font='arial 28 bold')
    lblps.pack(padx=15,pady=15)
    pwd=Entry(log,textvariable=ep,bg='light pink',fg='black',width=20,font='arial 28 bold',relief=RAISED,show='*')
    pwd.pack(padx=5,pady=5)
    bfe=Button(log,text='LOGIN',bg='light pink',fg='black',font='arial 30 bold',relief=FLAT,
               command=enter1)
    bfe.pack(padx=20,pady=20)

    log.mainloop()
    
main=Tk()
main.title('Login window')
main.config(bg='black')
img=PhotoImage(file='ppp.png')
lbl=Label(main,image=img,relief=FLAT)
lbl.pack(expand=YES,fill=BOTH)
lbl2=Label(lbl,text='SELECT YOUR CHOICE',bg='gray',fg='black',font='arial 20 bold')
lbl2.pack(padx=15,pady=15)
bfl=Button(lbl,text='LOGIN',bg='gray',fg='black',font='arial 30 bold',relief=FLAT,width=20,command=log)
bfl.pack(padx=20,pady=20)
bfl.bind("<Enter>",displaybfl)
bfl.bind("<Leave>",displaybfl1)
bfr=Button(lbl,text='REGISTER',bg='gray',fg='black',font='arial 30 bold',relief=FLAT,width=20,
                                                command=reg)
bfr.pack(padx=20,pady=20)
bfr.bind("<Enter>",displaybfr)
bfr.bind("<Leave>",displaybfr1)
main.mainloop()

    
