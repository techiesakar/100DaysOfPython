# If the bill as $150.00, 12% tip amount, 5 people to split bill
print("Welcome to Tip Calculator")
bill_amount = float(input("Enter the total bill : "))
tip_per = float(input("Enter the tip percent you want to give : "))
total_people = int(input("Total people to split the bill : "))
tip_amt = tip_per/100 * bill_amount
final_bill = bill_amount + tip_amt
# each_person_bill = round(final_bill/total_people, 3)
each_person_bill = "{:.3f}".format(final_bill/total_people)
print(f"Each person should pay : ${each_person_bill}")
