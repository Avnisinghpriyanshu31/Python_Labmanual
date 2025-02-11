#A program that calculate the area and perimeter of rectangle
while True:
    ch = input(
        "Name:- Avni singh SET-1B\n"
        "A program that calculate the area and perimeter of rectangle\n"
        "1. find area of rectangle\n"
        "2. find perimeter of rectangle\n"
        "3. Exit\n"
        "please enter your choice:"
        )
    if ch == '1':
       l =  float(input("Enter your length value:"))
       b = float(input("Enter your breadth value:"))
       print(" area of rectangle = ", l*b)
    elif ch =='2':
       l =  (input("Enter your length value:"))
       b = (input("Enter your breadth value:"))
       print("perimeter of rectangle = ",2*(l+b))
    elif ch =='3':
       print("Thank you!")
       break

    else:
        print("Please enter a valid choice...\n")