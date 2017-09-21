import random
print("_ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
print("\t\tGUESS THE NUMBER APP")
print("_ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
guess=4
number =random.randint(0,100)
while guess!=number:
	print("Guess a number between 0 and 100: ",end=' ')
	guess=int(input())
	number =random.randint(0,100)
	if guess<number:
		print(str("Sorry but ") + str(guess) + str(" is LOWER than the number"))
	elif guess > number:
		print(str("Sorry but ") + str(guess) + str(" is HIGHER than the number"))
	elif guess == number:
		print(str("YES! You've got it. The number was ") + str(guess))


	