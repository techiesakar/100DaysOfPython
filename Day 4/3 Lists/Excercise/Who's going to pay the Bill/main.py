import random
name_string = input("Give me everybody's name, seperated by comma. ")
names = name_string.split(", ")
# have_to_pay = random.randint(0, len(names)-1)
# print(names[have_to_pay] + " is going to buy the meal today")
have_to_pay = random.choice(names)
print(have_to_pay + " is going to buy the meal today")
