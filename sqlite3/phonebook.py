from cgitb import text
from email import message
import sqlite3
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Banco de Dados")
window.geometry("500x500")

with sqlite3.connect("phonebook.db") as db:
    cursor = db.cursor() 
def createTable():
    cursor.execute(""" CREATE TABLE IF NOT EXISTS Names(id integer PRIMARY KEY AUTOINCREMENT,firstname text,surname text,
    phonenumber text);
    """)
def addDates():
    name = nameBox.get()
    surname = surnameBox.get()
    phonenumber = phonenumberBox.get()
    cursor.execute(f""" INSERT INTO Names(firstname,surname,phonenumber)
    VALUES('{name}','{surname}','{phonenumber}')""")
    db.commit()

def deleteAll():
    cursor.execute("DELETE FROM Names;")
    nameList = f'Deleted {cursor.rowcount} Rows'
    messagebox.showinfo('Delete window',nameList)
    db.commit()

buttonDb = Button(text="Create\nDatabase",command= createTable)
buttonDb.place(x=50,y=25,width=100,height=50)

labelName = Label(text= "Enter the student firstname:")
labelName.place(x=20,y=100)
nameBox = Entry()
nameBox.place(x=200,y=100)

labelSurname = Label(text= "Enter the student surname:")
labelSurname.place(x=20,y=150)
surnameBox = Entry()
surnameBox.place(x=200,y=150)

labelPhonenumber = Label(text= "Enter the student phone number:")
labelPhonenumber.place(x=20,y=200)
phonenumberBox = Entry()
phonenumberBox.place(x=200,y=200)

button = Button(text="Save",command= addDates)
button.place(x=210,y=250,width=100,height=25)

button = Button(text="Delete\nall data",command= deleteAll)
button.place(x=50,y=250,width=100,height=40)

window.mainloop()
db.close()