from tkinter import *
def convert1():
    km = entry_box.get()
    km = float(km)
    miles = km * 0.6214
    miles = round(miles,5)
    entry_box.delete(0,END)
    entry_box.insert(END,miles)

def convert2():
    miles= entry_box.get()
    miles = float(miles)
    km = miles * 1.6093
    km = round(km,5)
    entry_box.delete(0,END)
    entry_box.insert(END,km)

window = Tk()
window.geometry("300x200")
entry_box = Entry(text= "")
entry_box.place(x=50,y=10,width=80,height=25)
entry_box.focus()
button_Mi = Button(text = "Miles to km",command=convert2)
button_Mi.place(x=50,y=60,width=75, height=25)
buttonKm = Button(text = "Km to miles",command=convert1)
buttonKm.place(x=50,y=35,width=75, height=25)
window.mainloop()
