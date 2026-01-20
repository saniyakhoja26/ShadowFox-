"""
Task Level: Beginner
Internship: ShadowFox Python Development
Name: Saniya Khoja
Task: List - Justice League

"""

# Initial Justice League list
justice_league = [ "Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern" ]

print("Initial Justice League:", justice_league)

# 1. Number of members
print("\nNumber of members in Justice League:", len(justice_league))

print("\n---------------------------------------\n")

# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding Batgirl and Nightwing:", justice_league)

print("\n---------------------------------------\n")

# 3. Make Wonder Woman the leader (move to beginning)

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After making Wonder Woman the leader: ", justice_league)

print("\n---------------------------------------\n")

# 4. Separate Aquaman and Flash
# Moving Green Lantern between them

justice_league.remove("Green Lantern")

flash_index= justice_league.index("Flash")
justice_league.insert(flash_index, "Green Lantern")

print("After separating Aquaman and Flash: ", justice_league)

print("\n---------------------------------------\n")

# 5. Replace the list with new team members
justice_league= [ "Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow" ]

print("After replacing team with new members: ", justice_league)

print("\n---------------------------------------\n")

# 6. Sort the Justice League alphabetically
justice_league.sort()
print("Sorted Justice League: ", justice_league)

# Bonus Question
print("\nNew leader of Justice League: ", justice_league[0])