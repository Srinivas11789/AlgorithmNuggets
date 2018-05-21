class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        """
        # Brute force - Time limit exceeded
        result = []
        i = 0
        while len(result) <= n:
            result.extend(list(str(i)))
            i += 1
        return int(result[n])
        """
        
        # Optimize                    0       1       2   3   4   5 . 6 . 7 . 8 . 9       10,      10+1    
        # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,      11,     12, 13, 14, 15, 16, 17, 18, 19,     20,      21       30
        # 1, 2, 3, 4, 5, 6, 7, 8, 9, (10,11), (12,13) (14,15)....................(28,29) (30,31)  (32,33)  (50,51)
        # 10, 30, 50, 70, 90 for 2 digits
        
        # Obvious case
        if n < 10:
            return n
        
        # Within 9 or <10 it is easier to calculate, possible reduction to the value being within 9
        # Reference from https://www.programcreek.com/2014/09/leetcode-nth-digit-java/ - a mathematical solution
        """
        Regularity:
            1 - 9  : 9
            10 - 99 : 90 * 2
            100 - 999 : 900 * 3
            1000 - 9999 : 9000 * 4
         
        For example given n is 1000, we first -9 and then -180. The left is 811. The number is 100+810/3=370. The digit is the (810%3=0)th. Therefore, the digit is 3.
        """
        
        # For first 1 - 9
        start = 1
        count = 9
        length = 1
        
        # Iterate for 10-99, 100-999......
        while n > length*count:
            # Subtract all the previous range values as we progress
            n = n - (length*count)
            
            # Update length start and end for increasing ranges
            length += 1
            count *= 10
            start *= 10
            
            #print n, length, count, start
            
        start = start + (n-1)//length
        
        return int(str(start)[(n-1)%length])
        
        """
        # Fails for 1000
        # Logic - Create a boundary and then nail it. The round off numbers like 10, 20, 30, 40 occurs at 5s and 10s, calculate the nearest such entry and create a boundary to nail down the digit
        # Even numbered ten's like 20 40 60 appear at 5s and odd numbered appear at 10 30 50s
        # 
        
        # Given a number, find the nearest 10s 20s 
        nearest = str(n)[:-1]+"0"
        #nearest = str(n)[:2]+"0"
        
        # From 5 - 10
        if int(nearest[:-1])%2 == 0:
            roundOff = int(str(int(nearest[:-1])//2)+"5")
            resultInd = n - int(nearest)
            result = "".join([str(i) for i in range(roundOff,roundOff+5)])[resultInd]
        # From 1 - 5
        else:
            roundOff = int(str((int(nearest[:-1])//2)+1)+"0")
            resultInd = n - int(nearest)
            result = "".join([str(i) for i in range(roundOff,roundOff+5)])[resultInd]
        
        return int(result)
        """
        
        """
        # tried math hacks to calculate
        d = len(str(n))
        
        if n%5 == 0:
            
        if n%d == 0:
            a = n - int(str(n)[-1])//d
            print n,a,c
            return int(str(a)[0])
            #n = n - int(str(n)[-1])//d
            #return int(str(n)[0])
        else:
            # n = 13, a = 11, 
            c = n-(d-1)
            a = c - int(str(c)[-1])//d
            print n,a,c
            return int(str(a)[n-c])
        """
        
        """
        # Every length of number is going to be a arithmetic progression, for example - 10 -> 99, 100 -> 999 where the start element a will be 10 or 100 and the interval will be d = 2 or 3
        
        # Length of intreval the difference is
        d = len(n)
        
        # First element is
        a = int("1"+"0"*(d-1))
        
        # Could create a arithmetic progression a, d, tn = a+(n-1)d
        nth_element = a + (n-1)*d
        
        # Example:
        # n = 11, result = 0
        # a = 10, d = 2, 10+2*10 => 30
        """
        
        
        
        
        
    
    
        
