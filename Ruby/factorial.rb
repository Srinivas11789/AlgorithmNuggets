#Ruby Factorial program 
#Function to call the factorial of the program
def fact(n)
#Check to return 1 if the given number is 0
	if n == 0
  		1
 	else
#Condition to find the factorial of a program
  	if n> 0
   		n * fact(n-1)
   	else 
   		puts "no factorial for -ve number"
  	end
	end   
end

#Getting the input from user
input = Integer(gets.chomp)

#print statement to print the factorial
puts fact(ARGV[0].to_i)
