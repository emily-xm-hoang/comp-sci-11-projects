"""
## Data Analysis Assignment - "Gotta Have" Checklist
### Name: Emily Hoang
### Total: 44 / 45

- Well done! Your programs alwaysh have a personal flair that make things interesting
- Best to avoid line numbers in comments since it's easy for those to change if lines are added/removed from code.
- Missing .lower() on the other classmate input, which means that if the user types in a name that includes upper case, this won't match, and then the program laughs as though the user lacks intelligence :(
 
- [X] **0. Data Handling**  
  Properly loads and processes data from `responses.csv`  with Python
 
- [X] **1. Algorithm Design**  
  Clear and logical algorithm design written in English before coding.
  *Advanced Criteria:* The algorithm is efficient and avoids unnecessary computations.
 
- [X] **2. Use of Comparison Operators**  
  Effectively uses comparison operators (`<`, `>`, `<=`, `>=`) to analyze data.  
  *Advanced Criteria:* Incorporates multiple or more advanced comparisons in its analysis.
 
- [X] **3. Observations Made**  
  At least **2 interesting observations** are made based on the data analysis.
  *Advanced Criteria:* Draws connections between observations and real-world implications.
 
- [X] **4. User Interaction**  
  Implements user input to enhance interactivity and engagement with the program.
  *Advanced Criteria:* Provides a user-friendly interface with clear and robust prompts.
 
- [X] **5. Code Quality**  
  Code is well-organized, readable, and follows Python naming conventions for descriptive variable names.
  *Advanced Criteria:* Uses best practices to improve readability.
 
- [X] **6. Comments and Documentation**  
  Includes meaningful comments that explain the logic and steps taken in the code.
  *Advanced Criteria:* Comments are thorough and enhance understanding of the code; comments don't just repeat what the code does.
 
- [X] **7. Testing**  
  Code is tested thoroughly, with evidence of testing documented in comments.
  *Advanced Criteria:* Includes test cases and description of how the program was validated.
 
- [X] **8. Validation**  
  The code correctly implements the documented algorithm design. The program does what you say it will do!
  *Advanced Criteria:* The program meets the defined objectives and delivers the intended value to its users.
 
- [3] **9. Error Handling**  
  Implements basic error handling to manage potential issues (e.g., use of strip()).
  *Advanced Criteria:* Advanced error handling that anticipates user mistakes.
 
- [X] **10. Creativity and Originality**  
  Shows creativity in the approach or analysis, going beyond basic requirements.  
  *Advanced Criteria:* Introduces unique features or innovative analysis methods.
 
- [X] **11. Version Control (2 points)**  
  Source code is committed to repository on Github within a folder for unit 2.5 (e.g. )
"""
file = open("2.5/responses.csv") # opens the csv file

junk = file.readline() # reads and discards header of csv file: topics of data collected

people = {} # makes an empty dictionary to store all the lists for later

for line in file: # for loop for each line in the file

  # reads each line of the file, lowercasing everything, stripping unwanted characters, and splitting each value into a string within a list
  data = line.lower().strip(" \n,!?").split(",")
  # print(data) - for testing
  names = data[4] # name the current list after the person
  people[names]= data # store the person's data into their own list INTO the dictionary
  data.pop(5) # deletes the empty string in the list because unnecessary
  del data[0:4] # deletes the user's id, start time, completion time, and email from the list because unnecessary

file.close() # closing the file to avoid crashes

# line 70 to 72 collects user input for their name and their classmates's name
print("\n~ Similarity Matching for Classmates \n**Disclaimer: this is not a compatibility calculator for dating ;-;")
user_name = input("\nEnter in your first and last name: ").lower().strip(" ,.!?")
classmate_name = input("Enter in your classmate's first and last name: ").strip(" ,.!?")

if user_name in people: # checks if the user's name is in the directory
  if classmate_name in people: # checks if the classmate's name is in the directory
    score = 0 # sets score to 0
    # print(str(people[user_name]) + "\n\n" + str(people[classmate_name])) - for testing
    for similarity in people[user_name]: # for loop and if statement for check for similiarties between the two
      if similarity in people[classmate_name]:
          score += 1 # score goes up by 1 if there is a similarity between the two
          # print(similarity) - for testing
    
    print("Your score with " + str(classmate_name) + " is " + str(score) + "/11") # prints score out of 11
    
    highest_score = 0 # initializes the score of the highest match to 0 
    best_match = "" # sets the person with the best match as an empty string to store name later
    for person in people: # loops through everyone in the dictionary
      if person != user_name: # doesn't include the user themself, otherwise it will always return as themselves as the highest match
        current_score = 0 # initializes score of the current person being compared to the user to 0
        for answer in people[user_name]: # for loop in which every matching answer gains 1 point to the current score
          if answer in people[person]:
              current_score +=1
        if current_score > highest_score: # if the current person's score is greater than the high score
          highest_score = current_score # then it is replaced 
          best_match = person # the current person now is the best match for the user
        elif current_score == highest_score: # in the case there are multiple people who share the same high score
          best_match = best_match + ", " + str(person) # concat them onto the list of people with the high score
    print("\nYour best match(es) is/are " + str(best_match))
    print("Your score with "  + str(best_match) + " is " + str(highest_score) + "/11")

    import random 
    if score <= 2: # if the score is equal to or less than 2, the user has an option to FIGHT THEIR CLASSMATE MWAHAHHAHAHHAH
      print("\nYou and " + str(classmate_name)  +" must be enemies... fight? (yes/no)")
      answer = input().lower().strip(" ,.!?") # takes user input
      if answer == "yes": # if user says yes to fight
          situations = ["\nThe fight: You are up against " + str(classmate_name) + " in the finals for the school's annual pushup contest. "  \
          "\nHowever, you broke your arm yesterday after the semis because you fell off from the bleachers from celebrating.\n" \
          "Unfortunately, you lose 7-102 because the huge cast prevented you from bending your elbow.\n" \
          "What a shame!", "\nThe fight: You are battling it out for first in the national cha cha dancing championships.\n" \
          "In the admist of the dim room, your bald head shines like a disco ball and attracts the judges' attention.\n" \
          "You receive perfect 10's across the scoreboard while " + str(classmate_name) + " weeps in the corner after losing.\nBOO HOO."]
          outcome = random.choice(situations) # randomizes the fight siutation
          print(outcome)
      elif answer == "no": # if users says no
        print("... ok.")
      else:
        print("Partypooper :(")
    elif score >= 3 and score <=7:
      print("\nYou and " + str(classmate_name) + " can be friends (I think), yay!")
    elif score >= 8 and score <=11:
      print("\nTelepathy much...?")
    elif score == 12:
      print("\nYOU'RE THE SAME PERSON, haha you can't fool me.")
  else: # if the ALLEGED CLASSMATE is not in the directory
    print("Are you sure " + str(classmate_name) + " is in your class??? LOL")
else: # if the user is not in the directory
  print("How do you not even know your own name bruh -_-")

""" 
Test case:
@emily-xm-hoang ➜ /workspaces/using-github-emily-xm-hoang (main) $ /home/codespace/.python/current/bin/python /workspaces/using-github-emily-xm-hoang/2.5/data_analysis.py

~ Similarity Matching for Classmates 
**Disclaimer: this is not a compatibility calculator for dating ;-;

Enter in your first and last name: yuki li
Enter in your classmate's first and last name: orlando marchetto
Your score with orlando marchetto is 2/11

Your best match(es) is/are grace cha, hanny nguyen, santiago anabalon delpino, vivienne kam, andrew ta
Your score with grace cha, hanny nguyen, santiago anabalon delpino, vivienne kam, andrew ta is 5/11

You and orlando marchetto must be enemies... fight? (yes/no)
yes

The fight: You are battling it out for first in the national cha cha dancing championships.
In the admist of the dim room, your bald head shines like a disco ball and attracts the judges' attention.
You receive perfect 10's across the scoreboard while orlando marchetto weeps in the corner after losing.
BOO HOO.
"""
