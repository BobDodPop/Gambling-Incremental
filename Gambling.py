import random

points = 100
gambling = True
result = 0
min_roll = 1
max_roll = 100

print("Press enter to gamble")
print("Type guide for instructions")

while gambling? = True:
	roll = input("")
  if roll == "":
		roll = "."
		result = random.randint(min_roll, max_roll)
		points += result/100
		print("You gained", result/100, "points!"
