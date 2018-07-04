
#ASSIGNMENT-17(GUI)
#Q1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.

from tkinter  import *
import sys
def exit(): 
  sys.exit()
w=Tk()
l=Label(w,text="Hello World",width=50,bg="green",fg="red")
l.pack()
b=Button(w,text="Exit",width=25,bg="yellow",command=exit)
b.pack()
w.mainloop()


#Q2. Write a python program to in the same interface as above and create a action when the button is click it will display some text.

 from tkinter import *
hemu=Tk()
def closewindow():
  exit()
button=Button(hemu,text="close window",command=closewindow)
button.pack()
mainloop()






#Q3. Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.
 


from tkinter import *
hemu=Tk()
a=Frame(hemu)
a.pack()


Button(hemu,text="cars",bg="blue").pack()
def closewindow():
  exit()
Button(hemu,text="close window",bg="red",command=closewindow).pack()
mainloop()




#Q4.Write a python program using tkinter interface to take an input in the GUI program and print it

from tkinter import *
def show_entry_fields():
 print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
w = Tk()
Label(w, text="First Name").grid(row=0)
Label(w, text="Last Name").grid(row=1)

e1 = Entry(w)
e2 = Entry(w)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
b=Button(w, text='Quit', command=w.quit).grid(row=3, column=0, sticky=W,pady=4,)

c=Button(w, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )