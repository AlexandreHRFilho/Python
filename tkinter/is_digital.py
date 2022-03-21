from tkinter import *
import csv
def csvSave():
    file = open("saveFile.csv","w")
    tmp_list = num_list.get(0,END)
    item = 0
    for x in tmp_list:
        newrecord = tmp_list[item] + "\n"
        file.write(str(newrecord))
        item += 1
    file.close()
def add_num():
    num = entry_box.get()
    if num.isdigit():
        num_list.insert(END,num) 
        entry_box.delete(0,END)    
        entry_box.focus()   
    else:
        entry_box.delete(0,END)    
        entry_box.focus()
       
def clear_list():
    num_list.delete(0,END)
    entry_box.focus()
window = Tk()
window.geometry("300x150")
entry_box = Entry(text= "")
entry_box["justify"]= "center"
entry_box.place(x=100,y=10,width=100,height=25)
buttonAdd = Button(text="Add", command= add_num)
buttonClean = Button(text = "Clear", command=clear_list)
buttonAdd.place(x=200,y=10,width=35,height=25)
buttonClean.place(x=70,y=10,width=35,height=25)
num_list = Listbox()
num_list.place(x=100,y=50,width=100,height=150)
num_list["justify"] = "center"
buttonSave = Button(text="Save",command= csvSave)
buttonSave.place(x=235,y=10,width=25,height=25)
window.mainloop()