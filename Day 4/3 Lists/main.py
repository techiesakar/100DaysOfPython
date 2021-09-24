list_of_people = ["Sakar", "Daniel",
                  "Danver", "Samia", "Samir", "Seijel", "Sia"]
print(list_of_people[0])                   # Sakar
print(list_of_people[-1])                  # Sia
list_of_people[-2] = "Seijal"              # Seijel changed to Seijal
list_of_people.append("Tara")              # Append "Tara" to the last
list_of_people.extend(["Burno", "Javi"])   # Add Burno and Javi to the last
print(list_of_people)

# Lists inside list
boys = ["Sakar", "Daniel", "Danver", "Samir"]
girls = ["Samia", "Seijel", "Sia"]
combine_list = [boys, girls]
print(combine_list)
