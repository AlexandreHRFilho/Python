from tkinter import *
def addName():
    name = entry_box.get()
    name_list.insert(END,name)
    entry_box.delete(0,END)
    entry_box.focus()
def clear():
    name_list.delete(0,END)
    entry_box.focus()
window = Tk()
window.title("Name list")
window.geometry("400x200")
label= Label(text="Add a name in list:").place(x=10,y=10,width=150,height=25)
entry_box = Entry(text='')
entry_box.place(x=140,y=10,width=150,height=25)
entry_box.focus()
button = Button(text="Add",command=addName)
button.place(x=300,y=10,width=30,height=25)
name_list = Listbox()
name_list.place(x=140,y=40,width=150,height=150)
button2 = Button(text="Clear",command=clear)
button2.place(x=340,y=10,width=35,height=25)
window.mainloop()