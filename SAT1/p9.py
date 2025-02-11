while True:
    print(
        "Name: Avni Singh Priyanshu SET-1I\n"
        "A program that generates a multiplication table for a given number\n"
        "1. Find multiplication table\n"
        "2. Exit\n"
    )
    ch = input("Please enter your choice: ")

    if ch == "1": 
        number = int(input("Enter the number: "))
        print(f"Multiplication table for {number}:")
        for i in range(1, 11): 
            print(f"{number} x {i} = {number * i}")
    elif ch == "2": 
        print("Thank you!")
        break
    else: 
        print("Please enter a valid choice...\n")