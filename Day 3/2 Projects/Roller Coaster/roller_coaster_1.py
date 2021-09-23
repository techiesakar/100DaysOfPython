print("Welcome to Roller Coaster")
height = int(input("Enter your height in cm : "))
if height >= 120:
    age = int(input("Enter your age : "))
    if age > 18:
        print("Please pay $12 for ticket")
    elif age <= 18:
        print("Please pay $7 for ticket")
    else:
        print("Please pay $12 for ticket")
else:
    print("Sorry!, You've have to grow more taller to ride Roller Coaster")
