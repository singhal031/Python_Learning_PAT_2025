# Program to check if-else and nested conditions
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
    if num % 2 == 0:
        print("It is even.")
    else:
        print("It is odd.")
elif num < 0:
    print("The number is negative.")
    if num % 2 == 0:
        print("It is even.")
    else:
        print("It is odd.")
else:
    print("The number is zero.")
