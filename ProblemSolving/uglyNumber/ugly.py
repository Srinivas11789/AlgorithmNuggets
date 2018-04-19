class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        factors = [2,3,5]
        if num == 0:
            return False
        while num != 1:
            i = 0
            while num%factors[i] != 0:
                i = i + 1
                if i > 2:
                    return False
            num = num//factors[i]
        return True
                
        
