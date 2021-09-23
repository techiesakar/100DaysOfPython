# Input two digit number and add them

# Always takes string input
two_digit_number = input("Enter two digits number: ")
first_digit_number = two_digit_number[0]
second_digit_number = two_digit_number[1]

# Converting to integer
result = int(first_digit_number) + int(second_digit_number)
print(result)
