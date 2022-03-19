"""Menu created with subprograms concept"""
def add():
    name = input("Add a new name: ")
    names.append(name)
    return names
def change():
    num = 0
    for x in names:
        print(num,x)
        num +=1
    selection_num = int(input("Enter the number of the name you want to change: "))
    name = input("Enter new name: ")
    names[selection_num] = name
    return names
def del_():
    num = 0
    for x in names:
        print(num,x)
        num += 1
    selection_num = int(input("Enter the number of the name you want to delete: "))
    del names[selection_num]
    return names
def view():
    num = 0 
    for x in names:
        print(num,x)
        num += 1
    
def main():
    again_ = 'y'
    while again_ == 'y':
        print("\nMenu\n1- Add a name\n2- Change a name\n3 - Del a name\n4 - View names\n 5 Close the program")
        selection = int(input("Enter what you want to do: "))
        print("\n")
        if selection == 1:
            add()
        elif selection == 2:
            change()
        elif selection == 3:
            del_()
        elif selection == 4:
            view()
        elif selection == 5:
            again_ = 'n'
        else:
            print("Invalid option")

names = []
main()