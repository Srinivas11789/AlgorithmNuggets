#guess the number
#Import randint from random 
from random import randint

#Choose a random integer from 1 to 10
choo = randint(1,10)
print choo

#Declaring the user variable to 0 to start with the loop 
user = 0

#Check conditions and guess till it arrives at the expected value

while choo != user:
	user = int(raw_input("please enter a value between 1 to 10"))
	print user
	if choo < user:
		print ("please try a lower value")
	elif choo > user:
		print ("please try a higher value")
	
print ("correct guess")

