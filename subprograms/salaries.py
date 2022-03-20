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
def deleteRowRecord():
    file = open("Salaries.csv","r")
    tmp_file = []
    for row in file:
        tmp_file.append(row)
    file.close()
    x=0 # Lets possible see the line that user want to delete
    for row in tmp_file:
        print(x,row)
        x +=1
    rowTodelete = int(input("Enter the row number to delete: "))
    del tmp_file[rowTodelete]
    file = open("Salaries.csv","w")
    for row in tmp_file:
        file.write(row)
    file.close()
    


again = True
while again:
    print("\n1- Add to file\n2-View Records\n3-Delete a record\n4-Close the program")
    selection = int(input("Enter the number of your selection: "))
    print("\n")
    if selection == 1:
        addtofile()
    elif selection == 2:
        viewRecords()
    elif selection == 3:
        deleteRowRecord()
    elif selection == 4:
        again = False
    else:
        print("Invalid option")