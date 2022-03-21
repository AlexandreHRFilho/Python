from tkinter import *
import csv
def createFile():
    file = open("ages.csv",'w')
    file.close()
def saveFile():
    file = open("ages.csv",'a')
    name = name_box.get()
    age = age_box.get()
    newrecord = name + " " + age + "\n"
    file.write(str(newrecord))
    file.close()
    name_box.delete(0,END)
    age_box.delete(0,END)
    name_box.focus()

window = Tk()
window.geometry("400x100")

label1 = Label(text ="Enter a name")
label1.place(x=20,y=20,width=100,height=25)

name_box = Entry(text = '')
name_box.place(x=120,y=20,width=100,height=25)
name_box.focus()

label2 = Label(text = 'Enter a age')
label2.place(x=20,y=50,width=100,height=25)

age_box = Entry(text = '')
age_box.place(x=120,y=50,width=100,height=25)
age_box.focus()

button1 = Button(text = 'Create new file',command= createFile)
button1.place(x=250,y=20,width=100,height=25)

button2 = Button(text = 'Add to file',command=saveFile)
button2.place(x=250,y=50,width=100,height=25)

window.mainloop()