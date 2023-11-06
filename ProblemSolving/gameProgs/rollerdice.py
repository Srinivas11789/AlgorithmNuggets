#Roller dice program

from random import randint


#chooses a random integer from 1 to 6 for player1
player1 = randint(1,6)
print ("player1 chance",player1)


#chooses a random integer from 1 to 6 for player2
player2 = randint(1,6)
print("player2 chance",player2)

#Condition to check who wins
if player1 == player2:
	print("draw")
elif player1 > player2:
	print("player1 wins")
else:
	print("player2 wins")

