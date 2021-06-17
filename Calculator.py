import tkinter as tk
from tkinter import *
import math as m

root=tk.Tk()
root.title('Basic Calculator')

w,h = 640,250

d = Entry(root,width=40,borderwidth=5,bg='black',fg='white',insertbackground='white')
d.grid(row=0, column=0,padx=5, pady=10)

def click(n):
    d.insert(END,n)
def equal():
    r=d.get()
    result=eval(r)
    d.delete(0,END)
    d.insert(0,result)
def clear():
    d.delete(0,END)
def backspace():
    d.delete(len(d.get())-1)
    
f = Frame(root,width=w,height=h,bg='red')
f.grid(row=1,column=0,sticky='w',padx=10)

f1 = Frame(root,width=w,height=h,bg='red')
f1.grid(row=2,column=0,sticky='w',padx=10)

f2 = Frame(root,width=w,height=h,bg='red')
f2.grid(row=3,column=0,sticky='w',padx=10)

f3 = Frame(root,width=w,height=h,bg='red')
f3.grid(row=4,column=0,sticky='w',padx=10)

f4 = Frame(root,width=w,height=h,bg='red')
f4.grid(row=5,column=0,sticky='w',padx=10)

b7 = Button(f,text='7',width=8,height=2,relief='groove',bg='#ABA6A5',command=lambda:click(7))
b8 = Button(f,text='8',width=8,height=2,relief='groove',bg='#ABA6A5',command=lambda:click(8))
b9 = Button(f,text='9',width=8,height=2,relief='groove',bg='#ABA6A5',command=lambda:click(9))
bback = Button(f,text='b',width=8,height=2,relief='groove',bg='#8D9F81',command=backspace)


b4 = Button(f1,text='4',width=8,height=2,relief='groove',bg='#ABA6A5',command=lambda:click(4))
b5 = Button(f1,text='5',width=8,height=2,relief='groove',bg='#ABA6A5',command=lambda:click(5))
b6 = Button(f1,text='6',width=8,height=2,relief='groove',bg='#ABA6A5',command=lambda:click(6))
bd = Button(f1,text='/',width=8,height=2,relief='groove',bg='#6FD8D1',command=lambda:click('/'))


b1 = Button(f2,text='1',width=8,height=2,relief='groove',bg='#ABA6A5',command=lambda:click(1))
b2 = Button(f2,text='2',width=8,height=2,relief='groove',bg='#ABA6A5',command=lambda:click(2))
b3 = Button(f2,text='3',width=8,height=2,relief='groove',bg='#ABA6A5',command=lambda:click(3))
bp = Button(f2,text='*',width=8,height=2,relief='groove',bg='#6FD8D1',command=lambda:click('*'))


b0 = Button(f3,text='0',width=8,height=2,relief='groove',bg='#ABA6A5',command=lambda:click(0))
bdot = Button(f3,text='.',width=8,height=2,relief='groove',bg='#ABA6A5',command=lambda:click('.'))
be = Button(f3,text='=',width=8,height=2,relief='groove',bg='#8AB969',command=equal)
bm = Button(f3,text='-',width=8,height=2,relief='groove',bg='#6FD8D1',command=lambda:click('-'))


ba = Button(f4,text='+',width=8,height=2,relief='groove',bg='#6FD8D1',command=lambda:click('+'))
bclear = Button(f4,text='C',width=27,height=2,relief='groove',bg='#F4F7F2',command=clear)

b7.pack(side='left')
b8.pack(side='left')
b9.pack(side='left')
bback.pack(side='left')

b4.pack(side='left')
b5.pack(side='left')
b6.pack(side='left')
bd.pack(side='left')


b1.pack(side='left')
b2.pack(side='left')
b3.pack(side='left')
bp.pack(side='left')


b0.pack(side='left')
bdot.pack(side='left')
be.pack(side='left')
bm.pack(side='left')

bclear.pack(side='left')
ba.pack(side='left')

root.mainloop()