# Program to find Leap year of Not
year = int(input("Enter the year : "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("leap Year")
else:
    print("Not Leap year")
