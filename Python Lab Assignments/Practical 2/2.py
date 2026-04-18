# Enter 11 players
team = []
for i in range(11):
    name = input(f"Enter name of player {i+1}: ")
    height = float(input(f"Enter height (cm) of {name}: "))
    team.append({"name": name, "height": height})

# Find tallest player (max by height)
captain = max(team, key=lambda p: p["height"])

print("Captain of the team is:", captain["name"])
print("Height:", captain["height"], "cm")