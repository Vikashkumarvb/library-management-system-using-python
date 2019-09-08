from tkinter import *
import lib_data
import tkinter.messagebox
def display(e):
    e1['bg']='powder blue'
def display1(e):
    e1['bg']='blue'
def display2(e):
    e2['bg']='powder blue'
def display3(e):
    e2['bg']='blue'
def display4(e):
    e3['bg']='powder blue'
def display5(e):
    e3['bg']='blue'
def display6(e):
    e4['bg']='powder blue'
def display7(e):
    e4['bg']='blue'
def displayl(e):
    l['bg']='powder blue'
def displayl1(e):
    l['bg']='blue'
def displayb(e):
    b1['bg']='powder blue'
def displayb1(e):
    b1['bg']='blue'
def displayb2(e):
    b2['bg']='powder blue'
def displayb3(e):
    b2['bg']='blue'
def displayb4(e):
    b3['bg']='powder blue'
def displayb5(e):
    b3['bg']='blue'
def displayb6(e):
    b4['bg']='powder blue'
def displayb7(e):
    b4['bg']='blue'
def displayb8(e):
    b5['bg']='powder blue'
def displayb9(e):
    b5['bg']='blue'
def displayb10(e):
    b6['bg']='powder blue'
def displayb11(e):
    b6['bg']='blue'
def c():
    global root
    root.destroy()
def s():
    global l,lb1,lb2,lb3,eb,ea,ey,e1,ei,e2,e3,e4,b1,b2,b3,b4,b5,b6
    a=int(ei.get())
    b=lib_data.select(a)
    l.delete(0,END)
    for row in b:
        l.insert(END,("{}  {}  {}  {}".format(*row)))
    lib_data.Close()
def d():
    global l,lb1,lb2,lb3,eb,ea,ey,e1,ei,e2,e3,e4,b1,b2,b3,b4,b5,b6
    t1=int(ei.get())
    lib_data.delete1(t1)
    
def u():
    global l,lb1,lb2,lb3,eb,ea,ey,e1,ei,e2,e3,e4,b1,b2,b3,b4,b5,b6
    t1=(eb.get(),ea.get(),ey.get(),ei.get())
    lib_data.update(t1)
    
def dis(e):
    global l,lb1,lb2,lb3,eb,ea,ey,e1,ei,e2,e3,e4,b1,b2,b3,b4,b5,b6
    try:
        t=l.curselection()
        t1=tuple(map(str,(l.get(t[0])).split(sep='  ')))
        eb.set(t1[0])
        ea.set(t1[1])
        ey.set(t1[2])
        ei.set(t1[3])
    except:
        pass
    
def v():
    global l,lb1,lb2,lb3,eb,ea,ey,e1,ei,e2,e3,e4,b1,b2,b3,b4,b5,b6
    l.delete(0,END)
    s=lib_data.view()
    for row in s:
        l.insert(END,("{}  {}  {}  {}".format(*row)))
    lib_data.Close()
    
def Clear():
    global l,lb1,lb2,lb3,eb,ea,ey,e1,ei,e2,e3,e4,b1,b2,b3,b4,b5,b6
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
def f():
    global l,lb1,lb2,lb3,eb,ea,ey,e1,ei,e2,e3,e4,b1,b2,b3,b4,b5,b6
    try:
        l.insert(END,(eb.get(),ea.get(),ey.get(),ei.get()))
        lib_data.insert1(eb.get(),ea.get(),ey.get(),ei.get())
        Clear()
    except Exception as e:
        print(e)
        tkinter.messagebox.showinfo('error','isbn exist already')
        Clear()
        l.delete(0,END)
def books(win):
    global l,lb1,lb2,lb3,eb,ea,ey,e1,ei,e2,e3,e4,b1,b2,b3,b4,b5,b6,root
    root=Toplevel(win)
    root.title('lib')
    root.config(bg='black')
    # label
    lb1=Label(root,bg='blue',fg='white',font='arial 20 bold', text='book',relief=RAISED)
    lb1.grid(row=0,column=0,sticky='news',padx=5,pady=5)

    lb2=Label(root,bg='blue',fg='white',font='arial 20 bold', text='author',relief=RAISED)
    lb2.grid(row=0,column=2,sticky='news',padx=5,pady=5)

    lb3=Label(root,bg='blue',fg='white',font='arial 20 bold', text='year',relief=RAISED)
    lb3.grid(row=1,column=0,sticky='news',padx=5,pady=5)

    lb3=Label(root,bg='blue',fg='white',font='arial 20 bold', text='isbn',relief=RAISED)
    lb3.grid(row=1,column=2,sticky='news',padx=5,pady=5)
    #entry
    eb=StringVar()
    ea=StringVar()
    ey=IntVar()
    ei=IntVar()
    e1=Entry(root,textvariable=eb,bg='blue',fg='white',font='arial 20 bold',relief=RAISED)
    e1.grid(row=0,column=1,sticky='news',padx=5,pady=5)
    e1.bind("<Enter>",display)
    e1.bind("<Leave>",display1)

    e2=Entry(root,textvariable=ea,bg='blue',fg='white',font='arial 20 bold',relief=RAISED)
    e2.grid(row=0,column=3,sticky='news',padx=5,pady=5)
    e2.bind("<Enter>",display2)
    e2.bind("<Leave>",display3)


    e3=Entry(root,textvariable=ey,bg='blue',fg='white',font='arial 20 bold',relief=RAISED)
    e3.grid(row=1,column=1,sticky='news',padx=5,pady=5)
    e3.bind("<Enter>",display4)
    e3.bind("<Leave>",display5)

    e4=Entry(root,textvariable=ei,bg='blue',fg='white',font='arial 20 bold',relief=RAISED)
    e4.grid(row=1,column=3,sticky='news',padx=5,pady=5)
    e4.bind("<Enter>",display6)
    e4.bind("<Leave>",display7)
    #ListBox
    l=Listbox(root,bg='blue',fg='white',font='arial 20 bold',relief=RAISED)
    l.grid(row=3,column=0,rowspan=6,columnspan=3,sticky='news',padx=5,pady=5)
    #l.bind("<<ListboxSelect>>",dis)
    #l.bind("<Enter>",displayl)
    #l.bind("<Leave>",displayl1)
    #Button
    b1=Button(root,text='view all',bg='blue',fg='white',font='arial 20 bold',relief=RAISED,command=v)
    b1.grid(row=3,column=3,sticky='news',pady=5)
    b1.bind("<Enter>",displayb)
    b1.bind("<Leave>",displayb1)

    b2=Button(root,text='update',bg='blue',fg='white',font='arial 20 bold',relief=RAISED,command=u)
    b2.grid(row=4,column=3,sticky='news',pady=5)
    b2.bind("<Enter>",displayb2)
    b2.bind("<Leave>",displayb3)

    b3=Button(root,text='add new',bg='blue',fg='white',font='arial 20 bold',relief=RAISED,
              command=f)
    b3.grid(row=5,column=3,sticky='news',pady=5)
    b3.bind("<Enter>",displayb4)
    b3.bind("<Leave>",displayb5)

    b4=Button(root,text='delete ',bg='blue',fg='white',font='arial 20 bold',relief=RAISED,command=d)
    b4.grid(row=6,column=3,sticky='news',pady=5)
    b4.bind("<Enter>",displayb6)
    b4.bind("<Leave>",displayb7)

    b5=Button(root,text='search',bg='blue',fg='white',font='arial 20 bold',relief=RAISED,command=s)
    b5.grid(row=7,column=3,sticky='news',pady=5)
    b5.bind("<Enter>",displayb8)
    b5.bind("<Leave>",displayb9)

    b6=Button(root,text='close',bg='blue',fg='white',font='arial 20 bold',relief=RAISED,command=c)
    b6.grid(row=8,column=3,sticky='news',pady=5)
    b6.bind("<Enter>",displayb10)
    b6.bind("<Leave>",displayb11)
    root.mainloop()

