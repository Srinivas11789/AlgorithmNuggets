class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        
        """
        # Brute force logic - Time Limit Exceeded
        for i in range(c+1):
            for j in range(i,c+1):
                #print i,j
                if i**2 + j**2 == c:
                    return True
        return False
        """
        
        """
        # Memory Issues
        for i in range(c+1):
            if i**2 <= c:
                for j in range(i,c+1):
                    if j**2 <= c:
                        if i**2 + j**2 == c:
                            return True
        return False
        """
        
        """
        # Time Limit Exceeded
        # Optimization - check how many square numbers exist within the range and then try adding them
        # using math and square root
        import math
        score = int(math.sqrt(c))
        perfect = []
        for i in range(score+1):
            # This condition if i**2 < c is satisfied by taking square root
                p = i**2
                if c-p in perfect:
                    return True
                else:
                    perfect.append(p)
        for n in perfect:
            if c-n in perfect:
                return True
        return False
        """
        
        # Nice logic - Optimization using while loop - 
        # * Decide on using while loop for more control -- practice
        # * think with respect to operations from a boundary values
        import math
        score = int(math.sqrt(c))
        i = 0
        j = score
        while i <= j:
            perfect = i**2 + j**2
            if perfect == c:
                return True
            if perfect > c:
                j -= 1
            else:
                i += 1
        return False
    
        
        
        
