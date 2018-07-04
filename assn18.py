#Q1. Create a dict with name and mobile number.Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list of keys in the dictionary.


from tkinter import *

def show():
    k = l.get(ACTIVE)
    v = d[k]

    l1.config(text=k)
    l2.config(text=v)

d = {'abc':123, 'def':321, 'ghi':345, 'jkl':12, 'hjt':32}
root = Tk()

l = Listbox(root)
l.pack(side=LEFT, fill=Y)


for k in d.keys():
    l.insert(END,k)

s = Scrollbar(root, command = l.yview)
s.pack(side=RIGHT, fill=Y)
l.config( yscrollcommand=s.set)

l1 = Label(root, text='name')
l1.pack()




#Q2. In the same tkinter file as created above, create a function to insert items into the dictionary.

from tkinter import *

def show():
    k = l.get(ACTIVE)
    v = d[k]

    l1.config(text=k)
    l2.config(text=v)

def insert():
    k = e1.get()
    v = e2.get()

    d[k] = v

    l.insert(END,k)
    print(d)

d = {'abc':123, 'def':321, 'ghi':345, 'jkl':12, 'hjt':32}
root = Tk()

l = Listbox(root)
l.pack(side=LEFT, fill=Y)


for k in d.keys():
    l.insert(END,k)

s = Scrollbar(root, command = l.yview)
s.pack(side=RIGHT, fill=Y)
l.config( yscrollcommand=s.set)

l1 = Label(root, text='name')
l1.pack()
l2 = Label(root, text='number')
l2.pack()

b1 = Button(root, text="show", command=show)
b1.pack()

e1 = Entry(root)
e1.pack()
e2 = Entry(root)
e2.pack()

b2 = Button(root, text="Insert!", command=insert)
b2.pack()
root.mainloop()