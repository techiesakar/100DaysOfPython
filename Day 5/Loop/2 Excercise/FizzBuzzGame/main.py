# Print from 1 to 100
# If number divisibe by 3 print "Fizz"
# If number divisibe by 5 print "Buzz"
# If number divisibe by 3 and 5 print "FizzBuzz"

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        number = "FizzBuzz"
    elif number % 3 == 0:
        number == "Fizz"
    elif number % 5 == 0:
        number = "Buzz"
    print(number)
