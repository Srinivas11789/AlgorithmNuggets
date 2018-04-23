### Lt easy - power of 2 - 100 pass

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        while n > 1 and n%2 == 0:
            n = n//2
        
        if n == 1:
            return True
        else:
            return False
            

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



