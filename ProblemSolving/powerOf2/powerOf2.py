

def pow2(n):
	if n%2 == 0:
           if n == 2:
           	return "Yes it is a power of 2"
	   else:
		return pow2(n/2)
	else:
           return "No it is not a power of 2"

def main():
	n = input("Enter a number:")
 	print pow2(n)

main()
