#Roller dice program

from random import randint



player1 = randint(1,6)
print ("player1 chance",player1)



player2 = randint(1,6)
print("player2 chance",player2)

if player1 == player2:
	print("draw")
elif player1 > player2:
	print("player1 wins")
else:
	print("player2 wins")

