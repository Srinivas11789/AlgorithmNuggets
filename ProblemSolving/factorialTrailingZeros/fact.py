class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        ### Math Trick Solution - Using 5s to find the trailing zeros
        
        init = 5
        count = 0
        while init <= n:
            count += n//init
            init = init * 5
        return count
        
        """
        # Brute Solution - Naive approach - time limit exceeded
        def fact(n):
            if n == 0:
                return 1
            elif n == 1:
                return 1
            else:
                return n * fact(n-1)

        value  = str(fact(n))
        #print value
        count = 0
        for char in value[::-1]:
            if char == "0":
                count += 1
            else:
                return count
        # This counts all the zeros -- question to count trailing zeros
        #return value.count("0")
        """
                
