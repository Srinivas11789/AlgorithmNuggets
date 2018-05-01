class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        """
        # Brute Force with some decision making
        # MemoryError
        score = num//2
        for i in range(score):
            if i**2 == num:
                return True
        return False
        """
        
        """
        # 100 pass - Perfect Square: Instead of checking square of all the number in the range, calculate the mid and find the last number which is less than the mid of the num. Square of that number must be the perfect square
        i = 1
        while i < num/i:
            i += 1
        if i*i == num:
            return True
        else:
            return False
        """
        # Newton Method
        x = num
        while x*x > num:
            x = (x + num/x)/2
        return x*x == num
        
        
    
