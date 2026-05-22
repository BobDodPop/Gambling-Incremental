import random

points = 0
gambling = True
result = 0
min_roll = 1
max_roll = 100

def gamble():
	choice = "."
	result = random.randint(min_roll, max_roll)
	points += result/100
	print("You gained", result/100, "points!")
	

print("Press enter to gamble")
print("Type guide for instructions")

while gambling == True:
	choice = input("").lower()
	if choice == "":
		gamble()
	if choice == "guide":
		print("Press enter to gamble")
		print("Type guide for instructions")
		print("Type i to view inventory")
		print("Type u to view upgrades")
		print("Type b 'upgrade name' 'amount' to buy an upgrade")
