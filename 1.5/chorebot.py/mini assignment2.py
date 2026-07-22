# Mini-assignment 2
# Requirements remain the same, but the topic has changed:

## Chorebot Mini-Assignment "Gotta Have" Checklist (10 / 10)
#Your chorebot will ask the user whether they've completed various chores, tally them up, and then report the number of chores completed.
#- [X] Code runs: Chatbot executes with the Run button.
#- [X] Functionality: Chatbot asks the user about at least 5 chores.
#- [X] Robustness: Uses at least 2 different string methods for robustness (e.g. strip(), lower())
#- [X] For loop: Contains a for loop
#- [X] Counting: Chatbot tracks user's score with an integer
#- [X] Reporting: Chatbot reports user's score at the end
#- [X] Algorithm Design/comments: Algorithm written in English prior to coding. Comments at each key section of code
#  - Okay but make sure to explain what the code actually does. E.g. instead of "for loop", say "Ask each user a question and count how many times the user replies 'yes'".
#- [X] Testing: Show key examples of chat logs that demonstrate testing done
#  - Make sure to include a copy of some sample chatlogs e.g.:
"""
Mom is coming home in an hour and you haven't done the chores!
You hastily do them and check the following:
Did you do the oil change for the car yet? no
Did you dance with the cows (wake up, it's the first of the month)? oops
Did you walk the chickens? yes
Did you paint the horse's toenails? i forgot
Did you dress up the pigs for tonight's party? yes
Your score is 2
"""
#- [X] Code Organization: Code is clean and well-organized.
#- [X] Submission: Code is committed and synced to Github in a file at 1.5/chorebot.py
 
#2026/2/10
#author: emily hoang
#purpose: chatbot (detmerines user's afterlife)

#greeting
print("\nMom is coming home in an hour and you haven't done the chores!\nYou hastily do them and check the following:")
score = 0

# list of questions
questions = ["Did you do the oil change for the car yet?", "Did you dance with the cows (wake up, it's the first of the month)?", "Did you walk the chickens?", "Did you paint the horse's toenails?", "Did you dress up the pigs for tonight's party?"]

# for loop 
for chores_done in questions:
    answer = input(chores_done + " ").strip(" .?!").lower()
    
# if the user answers yes, score goes up by one
    if answer == "yes":
        score += 1

# final score
print("Your score is " + str(score))
