#A program that calculates the factorial of a number.
while True:
    print(
        "Name: Avni Singh\nSET-1E\n"
        "A program that checks if a given year is a leap year\n"
        "1. Check leap year\n"
        "2. Exit\n"
    )
    ch = input("Enter your choice (1 or 2): ")
    
    if ch == '1':
        try:
            year = int(input("Enter the year: "))
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                print(f"{year} is a leap year.\n")
            else:
                print(f"{year} is not a leap year.\n")
        except ValueError:
            print("Invalid input. Please enter a valid year.\n")
    
    elif ch == '2':
        print("Thank you!")
        break  
    
    else:
        print("Please enter a valid choice...\n")
