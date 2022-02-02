#!/usr/bin/env python
# coding: utf-8

# In[9]:


from tkinter import *
root = Tk()
e = Entry(root,width = 40,borderwidth = 10)
e.grid(row =0,column=0,columnspan=5,padx = 15,pady = 25)

def add(n):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(n))

def delet():
    e.delet(0,END)

def plus():
    n1 = e.get()
    global math
    global n2
    math = "ADD"
    n2 = int(n1)
    e.delete(0,END)
    
def same():
    n3 = e.get()
    e.delete(0,END)
    
    if math == "ADD":
        e.insert(0,n2+int(n3))
        
    if math == "SUB":
        e.insert(0,n2-int(n3))
        
    if math == "MUL":
        e.insert(0,n2*int(n3))
        
    if math == "DIV":
        e.insert(0,n2/int(n3))
        
    
def sub():
    n1 = e.get()
    global math
    global n2
    math = "SUB"
    n2 = int(n3)
    e.delete(0,END)
    
def mul():
    n1 = e.get()
    global math
    global n2
    math = "MUL"
    n2 = int(n1)
    e.delete(0,END)
    
def div():
    n1 = e.get()
    global math
    global n2
    math = "DIV"
    n2 = int(n2)
    e.delete(0,END)
    
    
button1 = Button(root,text = "1",padx = 60,pady=50,command = lambda:add(1))
button2 = Button(root,text = "2",padx = 60,pady=50,command = lambda:add(2))
button3 = Button(root,text = "3",padx = 60,pady=50,command = lambda:add(3))
button4 = Button(root,text = "4",padx = 60,pady=50,command = lambda:add(4))
    
button5 = Button(root,text = "5",padx = 60,pady=50,command = lambda:add(5))
button6 = Button(root,text = "6",padx = 60,pady=50,command = lambda:add(6))
button7 = Button(root,text = "7",padx = 60,pady=50,command = lambda:add(7))
button8 = Button(root,text = "8",padx = 60,pady=50,command = lambda:add(8))

button9 = Button(root,text = "9",padx = 60,pady = 50,command = lambda:add(9))
button0 = Button(root,text = "0",padx = 60,pady = 50,command = lambda:add(0))
same = Button(root,text="=",padx = 80,pady = 20,command = same)

delet = Button(root,text="clear",padx = 80,pady = 20,command = delet)

plus = Button(root,text = "+",padx = 60,pady = 50,command = plus)
sub = Button(root,text = "-",padx = 60,pady = 50,command = sub)
mul = Button(root,text = "x",padx = 60,pady = 50,command = mul)
div = Button(root,text = "/",padx = 60,pady = 50,command = div)

button1.grid(row = 1,column =0)
button2.grid(row = 1,column =1)
button3.grid(row = 1,column =2)
button4.grid(row = 2,column =0)



button5.grid(row = 2,column =1)
button6.grid(row = 2,column =2)
button7.grid(row = 3,column =0)
button8.grid(row = 3,column =1)
button9.grid(row = 3,column =2)

button0.grid(row = 4,column =0)
plus.grid(row = 4,column =1)
sub.grid(row = 4,column = 2)
div.grid(row = 5,column = 0)
mul.grid(row = 5,column = 1)

same.grid(row = 5,column = 2)
delet.grid(row = 6,column = 2)

root.mainloop()


# In[ ]:


#ITS RUNNING TIME

