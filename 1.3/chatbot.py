#chatbot assignment

#question 1
print ('What is your name?')
name = input()
#list
reply = ["Nice to meet you, ", "Heyyyyyy ", "Eww get away from me "]
import random
random_reply = random.choice(reply)
print (random_reply + name + "!")

#question 2
print ("How do you like your eggs served?")
input()
#list
comments = ["Um... ok ;-;", "Me too!", "No offense but that's weird.", "Oh... I don't like eggs."]
import random
random_comment= random.choice(comments)
print(random_comment)

#question 3
print("Are you single?")
response = input()
if response == "yes":
    print("AHAHHAHHAHAHAHAH CAN'T RELATE")
elif response == "no":
    print("WHOOOOOOOOOO OMGMGGMG PLS TELLL")
else:
    print("Why are you avoiding the question...")
