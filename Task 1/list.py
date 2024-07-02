# 1. You have a list of superheroes representing the Justice League. 

justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

#   Perform the following tasks:

# 1. Calculate the number of members in the Justice League.
justice_league = ["Superman","Batman","WonderWoman","Flash","Aquaman","Green Lantern"]
length=len(justice_league)
print(f"the total number of members are {length}")

# 2. Batman recruited Batgirl and Nightwing as new members. Add them to your list.
justice_league = ["Superman","Batman","WonderWoman","Flash","Aquaman","Green Lantern"]
justice_league.append("Badgirl")
justice_league.append("Nightwing")
print(justice_league)

# 3. Wonder Woman is now the leader of the Justice League. Move her to the beginning of the list.
justice_league = ["Superman","Batman","WonderWoman","Flash","Aquaman","Green Lantern"]
justice_league.remove("WonderWoman")
justice_league.insert(0,"WonderWoman")
print(justice_league)

# 4. Aquaman and Flash are having conflicts, and you need to separate them. 
#    Choose either "Green Lantern" or "Superman" and move them in between Aquaman and Flash.
justice_league = ["Superman","Batman","WonderWoman","Flash","Aquaman","Green Lantern"]
justice_league.remove("Superman")
justice_league.insert(3,"Superman")
print(justice_league)


# 5. The Justice League faced a crisis, and Superman decided to assemble a new team. 
#   Replace the existing list with the following new members: "Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow".
justice_league = ["Superman","Batman","WonderWoman","Flash","Aquaman","Green Lantern"]
justice_league.clear()
justice_league= justice_league +[ "Cyborg","Shazam","Hawkgirl","MartianManhunter","Green Arrow"]
print(justice_league)

# 6. Sort the Justice League alphabetically. The hero at the 0th index will become the new leader.
justice_league = ["Superman","Batman","WonderWoman","Flash","Aquaman","Green Lantern"]
justice_league.sort()
print(justice_league)

# BONUS: Can you predict who the new leader will be?

print(f"The Leader of Justice League is {justice_league[0]}")