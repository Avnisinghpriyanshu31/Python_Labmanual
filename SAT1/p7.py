while True:
    print(
        "Name : Avni sinh Priyanshu SAT-1g\n"
        "A program that checks if a given string is a palindrome\n"
        "1. Check palindrome\n"
        "2. Exit\n"
    )
    ch = input("Please enter your choice: ")

    if ch == "1": 
        string = input("Enter a string to check if it's a palindrome: ")
        if string == string[::-1]: 
              print(f"'{string}' is a palindrome.")
        else:
            print(f"'{string}' is not a palindrome.")
    elif ch == "2":  
        print("Thank you!")
        break
    else:  
        print("Invalid choice. Please enter a valid option.\n")