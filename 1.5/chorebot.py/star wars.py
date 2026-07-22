print("Today, you will face your destiny!!!")
x = input("Do you like capes? ").strip(" .?!").lower()
y = input("Do you like red? " ).strip(" .?!").lower()
if x == "yes" or y == "yes":
    print("Welcome to the dark side >:)")
else:
    print("Welcome to the light side")