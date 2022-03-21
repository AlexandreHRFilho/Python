from tkinter import *


def addtoTotal():
    answer = int(display["text"])
    num = input_entry.get()
    if num == "":
        num = 0
    total = int(num) + answer 
    display["text"] =int(total)
    input_entry.delete(0,END)
def reset():
    global total
    total = 0
    display["text"] = 0
    input_entry.delete(0,END)
    input_entry.focus()

total = 0
window = Tk()
window.title("Adding together")
window.geometry("200x200")
input_entry = Entry(text="")
input_entry.place(x=30,y=10,width=100,height=25)
button_add = Button(text="Add", command=addtoTotal)
button_add.place(x=30,y=30,width=50,height=25)
button_reset = Button(text="Reset", command=reset)
button_reset.place(x=80,y=30,width=50,height=25)
display= Message(text=0,relief="sunken")
display.place(x=30,y=110,width=100,height=30)

window.mainloop()