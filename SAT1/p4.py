lst = [] 
while True:
    print("Name-Avni singh \n SET-1D) Calculates the average of a list of numbers.")
    ch = input("1. Create List\n2. Calculate Average of List\n3. Exit\nEnter a Valid Choice: ")

    if ch == '1':
        lst = [12, 12, 15, 15]
        print("List created:", lst)

    elif ch == '2':
        if lst: 
            print("List:", lst)
            ave = sum(lst) / len(lst)
            print(f"Average of the list: {ave}")
        else:
            print("The list is empty. Please create the list first.")

    elif ch == '3':
        print("thank you!")
        break

    else:
        print("Enter a Valid Value \n\n")