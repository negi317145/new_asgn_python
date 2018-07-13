from tkinter import *
import pymysql

window=Tk()
window.title("Note Taking")



db=pymysql.connect("localhost",'window','hemoo317145','hemu')
cursor=db.cursor()


def add():
    add_window=Tk()
    list=[]


    def update():
        for i in list:
            mylist.insert("end",i)


    def save():
        sub = entry.get("1.0", END)
        notes = save_text.get("1.0", END)
        cursor.execute("insert into hemu values('" + sub+ "','" + notes + "');")
        db.commit()
        list.append(sub)
        update()


    label = Label(add_window, text="Subject", bg="blue", font="bold 18")
    label.place(x=20,y=10)
    entry=Text(add_window,height="2",width="45")
    entry.place(x=20,y=45)
    save_text=Text(add_window,height="30",width="60")
    save_text.place(x=20,y=90)
    save_button = Button(add_window, text="Save", font="bold 13", bg="green", fg="blue", command=save)
    save_button.place(x=390, y=45)
    add_window.minsize(600,600)



def show_all():
    show_window=Tk()
    show_window.minsize(600,600)
    qr=cursor.execute("select subject from hemu;")
    a=cursor.fetchall()
    for k in a:
        for p in i:
           
            print(p)



def search_notes():
    qr=cursor.execute("select subject from hemu")
    get_subject=cursor.fetchall()
    for i in range(len(get_subject)):
        list.append(get_subject[i][0])
    srch=search_entry.get("1.0",END)
    for subs in list:
        if srch==subs:
            fetchdata(notes)
            break


add_button=Button(window,text="Add New Note>>",font="bold 18",bg="blue",fg="black",command=add)
add_button.place(x=20,y=70)


list_all_notes_button=Button(window,text="List All Notes>>",font="bold 18",bg="blue",fg="black",command=show_all)
list_all_notes_button.place(x=300,y=70)


label=Label(window,text="Search Notes",font="bold 18")
label.place(x=20,y=20)


search_entry = Text(window,width=46,height="2")
search_entry.place(x=20,y=20)


search_button=Button(window,text="Search",font="bold 13",bg="red",fg="black",command=search_notes)
search_button.place(x=400,y=20)


label=Label(window,text="--Notes--",font="bold 20")
label.place(x=20,y=160)


scrollbar=Scrollbar(window,orient="vertical")
scrollbar.place(x=532,y=200,height=370)


mylist=Listbox(window,height="23",width="85",yscrollcommand=scrollbar.set)
mylist.place(x=20,y=200)



scrollbar.config(command=mylist.yview)


window.geometry("550x600")
window.resizable(False,False)
window.maxsize(600,600)
window.minsize(500,500)
window.mainloop()