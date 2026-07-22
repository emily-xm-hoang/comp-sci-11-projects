# takes order and outputs total cost
# asks burger for 5 dollars
# asks fries for 3 dollars
# outputs total with 14% tax

cost = 0
burger = input("DO YOU WANT BURGER 👹 (yes/no): ")
fries = input ("DO YOU WANT FRIES 👹 (yes/no): ")

if burger == "yes":
    cost += 5

if fries == "yes":
    cost += 3

final_cost = round((float(cost*1.14)), 4)

print("YO FINAL COST IS $" + str(final_cost) + "👹")