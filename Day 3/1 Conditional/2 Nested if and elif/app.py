# Program to check the greatest number using nested if
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))
num4 = int(input("Enter third number : "))


if num1 > num2:
    if num1 > num3:
        if num1 > num4:
            print(f"{num1} is greatest number")
        else:
            print(f"{num4} is greatest number")

elif num2 > num3:
    if num2 > num4:
        print(f"{num2} is greatest number")
    else:
        print(f"{num4} is greatest number")
elif num3 > num4:
    print(f"{num3} is greatest number")
else:
    print(f"{num4} is greatest number")
