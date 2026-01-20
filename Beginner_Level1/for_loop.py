"""
Task Level: Beginner
Internship: ShadowFox Python Development
Name: Saniya Khoja
Task: For Loop

"""

import random

# 1. Dice Roll Simulation
rolls= 20
count_6= 0
count_1= 0
two_sixes_in_row= 0

previous_roll= None

print("Rolling a six-sided die 20 times:\n")

for i in range(rolls):
    roll = random.randint(1, 6)
    print("Roll", i+1, ":", roll)

    if roll==6:
        count_6 +=1
        if previous_roll==6:
            two_sixes_in_row +=1
    
    if roll==1:
        count_1+=1

    previous_roll=roll

print("\nNumber of times 6 was rolled:", count_6)
print("Number of times 1 was rolled:", count_1)
print("Number of times two 6s appeared in a row:", two_sixes_in_row)

print("\n---------------------------------------\n")

# 2. Jumping Jacks Workout Program

total_jumping_jacks = 100
completed=0

while completed<total_jumping_jacks:
    completed+=10
    print("you completed", completed, "jumping jacks")

    if completed==total_jumping_jacks:
        print("congratulations! You completed the workout")
        break
    
    response = input("Are you tired? (yes/y or no/n): ").lower()

    if response=="yes" or response=="y":
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n):").lower()
        if skip =="yes" or skip=="y":
            print("You completed a total of", completed, "jumping jacks")
            break
    else:
        remaining = total_jumping_jacks - completed
        print(remaining, "jumping jacks are remaining")

print("\n---------------------------------------\n")
