"""
Task Level: Beginner
Internship: ShadowFox Python Development
Name: Saniya Khoja
Task: Variables

"""
# 1. Create a variable named pi and store the value 22/7
pi= 22/7
print("Value of pi: ",pi)
print("Data type of pi: ", type(pi))

print("\n---------------------------------------\n")


# 2. Create a variable called 'for' and observe the behavior
# This will cause an error because 'for' is a reserved keyword in Python

# Uncommenting the line below will raise a SyntaxError
# for = 4

print("You cannot use 'for' as a variable name because it is a python keyword.")

print("\n---------------------------------------\n")

# 3. Calculate Simple Interest
# Formula: Simple Interest = (P * R * T) / 100

Principal = 5000  # Principal amount
rate = 5          # Rate of interest
time = 3          # Time in years

simple_interest = (Principal*rate*time)/100

print("Principal Amount: ", Principal)
print("Rate of Interest: ", rate)
print("Time(years): ", time)

print("Simple Interest for 3 years is: ", simple_interest)

print("\n---------------------------------------\n")
