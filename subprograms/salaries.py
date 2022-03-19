import csv

def addtofile():
    file = open("Salaries.csv","a")
    name = input("Enter your name: ")
    salary = int(input("Enter salary: "))
    newRecord = name + ', '+ str(salary)+"\n"
    file.write(newRecord)
    file.close()
def viewRecords():
    file = open("Salaries.csv","r")
    for x in file:
        print(x)
    file.close()

again = True
while again:
    print("\n1- Add to file\n2-View Records\n3-Close the program")
    selection = int(input("Enter the number of your selection: "))
    print("\n")
    if selection == 1:
        addtofile()
    elif selection == 2:
        viewRecords()
    elif selection == 3:
        again = False
    else:
        print("Invalid option")