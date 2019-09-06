class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        """

        Logic 1: BruteForce technique - use all the permutation of arrangement and solve

	# Memoize
        primes = {1:False, 2:True}
        
	# Is a prime number?
        def is_prime(number):
            if number in primes:
                return primes[number]
            else:
                count = 0
                import math
                for i in range(2, int(math.sqrt(number))+1):#number//2+1):
                    if number%i == 0:
                        count += 1
                    if count >= 1:
                        primes[number] = False
                        return False
                primes[number] = True
                return True
        
	# Find if all Prime indices are with Prime Numbers?
        def are_prime_in_prime_index(array):
            
            #  Logic: Iterating all of the array - worst case --> time limit exceeded
            for i, item in enumerate(array):
                index = i+1
                prime_index = False
                prime_value = False
                # memoize for prime
                prime_index = is_prime(index)
                prime_value = is_prime(item)
                if not prime_index and not prime_value:
                    pass
                elif prime_index and prime_value:
                    pass
                else:
                    return False
            return True
            
	def are_prime_in_prime_index2(array):

            # Modified version of above logic
            # Logic 2: Taking into account some prime intelligence on array arrangement ( visit only prime index) --> time limit exceeded
            
            # Only even prime is 2
            #print(array)
            prime_index = is_prime(2)
            prime_value = is_prime(array[1])
            if prime_index and prime_value:
                pass
            else:
                return False
            # Array indexed one so every even index is odd index actually ( jump on even indexes from 2 which will be 3, 5, 7 )
            for i in range(2, len(array), 2):
                index = i+1
                item = array[i]
                #print(index, item)
                prime_index = False
                prime_value = False
                # memoize for prime
                prime_index = is_prime(index)
                prime_value = is_prime(item)
                if not prime_index and not prime_value:
                    pass
                elif prime_index and prime_value:
                    pass
                else:
                    return False
            return True
        
        integers = range(1, n+1)
        
        # Main program using the above functions - both fail with time limit exceeded
        # Get permutations
        import itertools
        count = 0
        for perms in itertools.permutations(integers):
            if are_prime_in_prime_index(perms):
                count += 1
        return count%((10**9)+7)
        

	# Logic 2 --> Completely different logic
	# * Visualize the properities and then solve
	# * Calculate the number of primes in N numbers and non primes
	# * for n=5, assume the indices and numbers are 1, 2, 3, 4, 5
        # * In this case, permutation would be 2 x 3 x 2 x 1 x 1 ( Reduce the primes=3 and non-primes=2, as you go over the positions
	# Which summarizes into factorial(3) * factorial(2) 

        # Logic 3: 83% faster and 100% space
        
        # Memoize primes and factorials to support recursion
        primes = {1:False, 2:True}
        factorials = {0:1, 1:1}
        
	# Is a prime number?
        def is_prime(number):
            if number in primes:
                return primes[number]
            else:
                count = 0
                import math
                for i in range(2, int(math.sqrt(number))+1):#number//2+1):
                    if number%i == 0:
                        count += 1
                    if count >= 1:
                        primes[number] = False
                        return False
                primes[number] = True
                return True
        
	# Factorial?
        def fact(number):
            if number not in factorials:
                factorials[number] = number * fact(number-1)
            return factorials[number]
        
        # Logic 3
        # * Count the number of primes in the range
        # * Know the indexes that are prime
        # * One iteration is enough for this case as the indexes and numbers are consecutive
        # * Use permutation problem --> 2 x 3 x 2 x 1 x 1

        primes_within_range  = []
        for i in range(2, n+1):
            if is_prime(i):
                primes_within_range.append(i)
        prime = len(primes_within_range)
        non_prime = 1+len(range(1,n))-prime
        print(prime, non_prime, fact(prime), fact(non_prime), primes_within_range)
        return (fact(prime)*fact(non_prime))%(10**9+7)
        
