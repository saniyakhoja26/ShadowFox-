"""
Task Level: Beginner
Internship: ShadowFox Python Development
Name: Saniya Khoja
Task: Numbers

"""

# 1. Using format() function
value = 145
representation = format(value, 'o')  # 'o' represents octal format

print("Original value:", value)
print("Formatted value using 'o':", representation)
print("Representation used: Octal")

print("\n---------------------------------------\n")

# 2. Area of a circular pond and water calculation
radius = 84                    # radius in meters
pi = 3.14

pond_area = pi*radius*radius   # Area of circle

print("Radius of pond: ", radius, "meters")
print("Area of the pond: ", pond_area, "square meters")

# Bonus Question
water_per_sqm = 1.4            # liters per square meter
total_water = pond_area * water_per_sqm

print("Total water in the pond (in liters):", int(total_water))

print("\n---------------------------------------\n")

# 3. Speed calculation
distance = 490                  # meters
time = 7*60                     # time in seconds 
speed = distance/time

print("Speed in meters per second: ", int(speed))

print("\n---------------------------------------\n")
