from tkinter import *
from money import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรเเกรมบันทึกข้อมูล')
GUI.geometry('500x400')

L1 = Label(G5UI,text='บันทึกความรู้', font= ('Angsana New',30),fg='green')
L1.place(x=30,y=40)

def Button2():
    messagebox.showinfo('เงินในบัญชี',my_account)

    
B1 = ttk.Button(GUI,text='มีเงินอยุ่กี่บาท')
B1.pack()

B2 = Button(GUI,text='มีเงินอยุ่กี่บาท',command=Button2)
B2.pack()






GUI.mainloop()
