# Add $3 more to bill, if people wan to take photo
print("Welcome to Roller Coaster")
height = int(input("Enter your height in cm : "))
bill = 0
if height >= 120:
    age = int(input("Enter your age : "))
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 12
    wants_photo = input("Do you want a photo taken ? Y or N :")
    if wants_photo == "Y":
        # Add $3 to their bill
        bill += 3
        print(f"Your bill is {bill}")
