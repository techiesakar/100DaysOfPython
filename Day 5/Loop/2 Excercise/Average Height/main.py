# Find the average height
student_heights = input("Input the height of the students :").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# print(student_heights)

# Method One
# total_heights = sum(student_heights)
# number_of_students = len(student_heights)
# average_heights = round(total_heights/number_of_students)
# print(average_heights)

# Good Way

total_height = 0
total_students = 0
for height in student_heights:
    total_height += height
    total_students += 1
print(total_height)
avg_height = round(total_height/total_students)
print(avg_height)
