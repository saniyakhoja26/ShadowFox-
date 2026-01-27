"""
Task Level: Beginner
Internship: ShadowFox Python Development
Name: Saniya Khoja
Task: Dictionary
"""

# 1. Friends Name and Length (List of Tuples)

friends = ["Alisha", "Hershey", "Nirmi", "Kevil", "Parv"]
friends_length = []

for name in friends:
    friends_length.append((name, len(name)))

print("Friends name with length:")
print(friends_length)

print("\n---------------------------------------\n")

# 2. Expense Tracking Using Dictionaries

my_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

#calculate total expenses 
my_total = sum(my_expenses.values())
partner_total = sum(partner_expenses.values())  

print("My total expenses:", my_total )
print("Partner's total expenses:", partner_total)   

#compare spending
if my_total > partner_total:
    print("I spent more than my partner.")  
elif partner_total > my_total:
    print("My partner spent more than me.")
else:
    print("We both spent the same amount.")


# Find category with maximum difference
max_difference = 0
difference_category = ""

for category in my_expenses:
    difference = abs(my_expenses[category] - partner_expenses[category])
    if difference > max_difference:
        max_difference = difference
        difference_category = category

print("Highest spending difference category:", difference_category)
print("Difference amount:", max_difference)

print("\n---------------------------------------\n")
