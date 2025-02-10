#A program that generates a random password of a specified length.
import random
import string

while True:
    print(
        "Name:- Avni Singh SET-1C\n"
        "A program that generates a random password of a specified length\n"
        "1. Find password\n"
        "2. Exit\n"
    )
    ch = input("Enter your choice (1 or 2): ")
    if ch == '1':
        l = int(input("Enter your desired password length: "))
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=l))
        print(f"Generated password: {password}")
    elif ch == '2':
        print("Thank you!")
        break
    else:
        print("Please enter a valid choice...\n")
