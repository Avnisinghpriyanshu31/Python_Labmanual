while True:
    print(
        "Name : Avni sinh Priyanshu SAT-1h\n"
        "A program that sorts a list of numbers in ascending or descending order\n"
        "1. Sort a list in ascending order\n"
        "2. Sort a list in descending order\n"
        "3. Exit\n"
    )
    ch = input("Please enter your choice: ")

    if ch == "1":  
        numbers = [1, 4, 6, 2, 8]
        print(f"Original list: {numbers}")
        sorted_numbers = sorted(numbers) 
        print(f"List in ascending order: {sorted_numbers}")
    elif ch == "2": 
        numbers = [1, 4, 6, 2, 8]
        print(f"Original list: {numbers}")
        sorted_numbers = sorted(numbers, reverse=True)  
        print(f"List in descending order: {sorted_numbers}")
    elif ch == "3": 
        print("Thank you!")
        break
    else:  
        print("Please enter a valid choice...\n")