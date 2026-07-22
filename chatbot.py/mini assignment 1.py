## Chatbot Mini-Assignment "Gotta Have" Checklist (10 / 10)

- Very ominous..!
 
#- [X] Code runs: Chatbot executes with the Run button.
#- [X] Functionality: Chatbot asks at least 3 questions.
#- [X] Listening: Chatbot uses an answer from the user in a response at least once
#- [X] If statement: Uses at least 1 if statement.
#- [X] Elif statement: Uses at least 1 elif statement.
#- [X] Else statement: Uses at least 1 else statement.
#- [X] Algorithm Design/comments: Algorithm written in English prior to coding.
#- [X] Testing: Show key examples of chat logs that demonstrate testing done
"""
Welcome to the afterlife...
Your final destination relies on your answers to the following questions:
1. Do you like cats or dogs? dogs
A happy person like you deserves to live in heaven and eternal happiness...
2. What is your favourite time of the day? cow
If you aren't a morning riser or night owl, then what are you...?
Let me guess, single. HAH!
3. What is one thing you regret not having done in life? doing good at school
doing good at school... I'm so sorry to hear that, I hope you can heal from all your pain in the afterlife.
I believe you still have much to fulfill within your soul, and therefore I have chosen for you to be reborn and seek a second chance at life.
"""

#- [X] Code Organization: Code is clean and well-organized.
#- [X] Submission: Code is committed and synced to Github


#2026/2/10
#author: emily hoang
#purpose: chatbot (detmerines user's afterlife)

#greeting
print("\nWelcome to the afterlife...\nYour final destination relies on your answers to the following questions:")
score = 0

# question 1
first_answer = input("1. Do you like cats or dogs? ")
if first_answer == "cats":
    print("I can tell you're a mysterious and introverted person... perhaps you suit somewhere else than heaven.")
    score += 1

elif first_answer == "dogs":
    print("A happy person like you deserves to live in heaven and eternal happiness...")
    score += 2

# question 2
second_answer = input("2. What is your favourite time of the day? ")
if second_answer == "morning":
    print("Imagine never sleeping in, I can't relate lol.")
    score += 0.5

elif second_answer == "afternoon":
    print("I guess that's when the sun is at it's peak, just like me.")
    score += 2

elif second_answer == "night":
    print("I'm guessing you pull all-nighters and not actual people.")
    score += 1
    
else:
    print("If you aren't a morning riser or night owl, then what are you...?\nLet me guess, single. HAH!")

# question 3
third_answer = input("3. What is one thing you regret not having done in life? ")
responses = ["I'm so sorry to hear that, I hope you can heal from all your pain in the afterlife.", "there will be a day where you can finally forgive yourself and put your soul at rest."]
import random
random_response = random.choice(responses)
print(third_answer + "... " + str(random_response))

if score >= 3:
    print("I have determined your final resting place.\n" \
    "I believe a good person like you deserves to forever live in peace and apart from harm, and therefore I choose: heaven.")

else:
    print("I believe you still have much to fulfill within your soul, " \
    "and therefore I have chosen for you to be reborn and seek a second chance at life.")
