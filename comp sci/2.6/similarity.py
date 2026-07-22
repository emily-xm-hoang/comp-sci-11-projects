print("Please enter hobbies, separated by spaces!")
hobbies1 = input("Person 1: ").split().lower()
hobbies2 = input("Person 2: ").split().lower()

for hobby in hobbies1:
    if hobby in hobbies2:
        score += 1
print("You have " + str(score) + " hobbies in common.")
 