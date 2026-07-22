score = 0
questions = ["eat? ", "study? ", "do your laundry?", "you call grandma?"]

for question in questions:
    answer = input("Did you " + question).strip(" .?!").lower()
    if answer == "yes":
        score += 1

if score == 0:
    print("I'm coming over.")

elif score in [1, 2]:
    print("Ok.")

else:
    print("Good!")