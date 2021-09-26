# Calculate the highest score from the list of scores
student_scores = input("Input a list of student :").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
heighest_score = 0
for score in student_scores:
    if score > heighest_score:
        heighest_score = score
print(f"The heighest score is {heighest_score}")
