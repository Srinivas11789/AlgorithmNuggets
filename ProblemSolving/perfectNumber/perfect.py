class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        # Time limit exceeded - [num: 20996011] when used to iterate through till num as well as iterate through till num//2. Use square root always for calculation of factors
        
        import math
        divisors = [1]
        if num <= 1:
            return False
        for i in range(2,int(math.sqrt(num))+1):
            if num%i == 0:
                if i not in divisors:
                    divisors.append(i)
                    divisors.append(num//i)
        if sum(divisors) == num:
            return True
        else:
            return False
        
        
