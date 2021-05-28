from tkinter import *
import ctypes
import os,time
from tkinter.ttk import Progressbar
from tkinter import filedialog

i=0
counter=1

class app:
    def __init__(self):
        self.root=Tk()
        self.root.geometry('288x60')
        self.root.maxsize(288,60)
        self.root.minsize(288,60)
        self.root.title("wall changer")
        self.button1=Button(text='start',width=3,height=1,command=self.start)
        self.button2=Button(text='clear',width=3,height=1,command=self.clear)
        self.button3=Button(text='quit',width=3,height=1,command=self.root.destroy)
        self.choose=Button(text='select',width=3,height=1,command=self.findpath)
        self.prog=Progressbar(length=100,orient="horizontal")
        self.delay=Entry(width=5)
        self.format=Entry(width=5)
        self.lab1=Label(text="Format:",fg="blue",bg="light green")
        self.lab2=Label(text="Delay:",fg="white",bg="red")
        self.lab3=Label(text="- from -",fg='yellow',bg='brown')

        self.lab1.place(x=0,y=0)
        self.format.place(x=50,y=0)
        self.lab2.place(x=0,y=30)
        self.delay.place(x=50,y=30)
        self.choose.place(x=100,y=0)
        self.button1.place(x=100,y=30)
        self.button2.place(x=140,y=0)
        self.button3.place(x=140,y=30)
        self.prog.place(x=180,y=30)
        self.lab3.place(x=200,y=5)
        self.root.mainloop()

    def start(self):
        global i,counter
        counter=1
        i=1
        self.prog['value']=0
        self.de=int(self.delay.get())
        self.form=self.format.get()
        if self.filenumber:
            self.apply()
        else:
            os.system("msg * Nothing found!")


    def clear(self):
        self.delay.delete(0,'end')
        self.format.delete(0,'end')
        self.path=""
        self.lab3.config(text="- from -")
    
    def findpath(self):
        self.path=filedialog.askdirectory()+"/"
        self.filenumber=len(os.listdir(self.path))


    def apply(self):
        global i,counter
        if i<=self.filenumber:
            fdir=self.path+f"{i}."+self.form
            self.lab3.config(text=f"{i} from {self.filenumber}")
            ctypes.windll.user32.SystemParametersInfoW(20,0,fdir,0)
            i+=1
            self.prog['value']=i*(100/self.filenumber)
            self.root.update_idletasks()
            if counter==self.filenumber:
                os.system("msg * Done!")
            counter+=1
            self.root.after(self.de*1000,self.apply)






app1=app()