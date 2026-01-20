"""
Task Level: Beginner
Internship: ShadowFox Python Development
Name: Saniya Khoja
Task: If Condition

"""

# 1. BMI Calculator
height = float(input("Enter your hegiht in meters: "))
weight = float(input("Enter you weight in kilograms: "))
bmi = weight/(height**2)

print("Your BMI is: ", round(bmi,2))

if bmi>=30:
    print("Obesity")
elif bmi>=25 and bmi<29:
    print("NOverweight")
elif bmi>=18.5 and bmi<25:
    print("Normal")
else:
    print("Underweight")

print("\n---------------------------------------\n")

# 2. City to Country Program
Australia = [ "Sydney", "Melbourne", "Brisbane", "Perth" ]
UAE = [ "Dubai", "Abu Dhabi", "Sharjah", "Ajman" ]
India = [ "Mumbai", "Bangalore", "Chennai", "Delhi" ]

city = input("Enter a city name: ")

if city in Australia:
    print(city, "is in Australia")
elif city in UAE:
    print(city, "is in UAE")
elif city in India:
    print(city, "is in India")
else:
    print("City not found in the database")

print("\n---------------------------------------\n")

# 3. Check if two cities belong to the same country
city1= input("Enter the first city: ")
city2= input("Enter the second city: ")

if city1 in Australia and city2 in Australia:
    print("Both cities are in Australia")
elif city1 in UAE and city2 in UAE:
    print("Both cities are in UAE")
elif city1 in India and city2 in India:
    print("Both cities are in India")
else:
    print("They don't belong to the same country")