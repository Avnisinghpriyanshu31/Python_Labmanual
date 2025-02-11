while True:
    print(
        "Name: Avni Singh\nSET-1F\n"
        "A program that calculates the factorial of a number\n"
        "1. Calculate factorial\n"
        "2. Exit\n"
    )
    ch = input("Enter your choice (1 or 2): ")
    
    if ch == '1':
        try:
            n = int(input("Enter the number: "))
            if n < 0:
                print("Factorial is not defined for negative numbers.\n")
            else:
                factorial = 1
                for i in range(1, n + 1):
                    factorial *= i
                print(f"Factorial of {n}: {factorial}\n")
        except ValueError:1
        print("Invalid input. Please enter a valid number.\n")
    
    elif ch == '2':
        print("Thank you!")
        break  
    else:
        print("Enter a valid choice...\n")