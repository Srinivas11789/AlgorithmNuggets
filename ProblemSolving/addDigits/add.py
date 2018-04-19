class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        # O(1) Logic - Solution: Digital Root
        # https://en.wikipedia.org/wiki/Digital_root
        if num == 0:
            return 0
        else:
            # Thought of a logic close to --> single digit == 0-9, hence if sum is greater than 9, then use the difference to calculate something -- Nice thought!! ==> 38 = 3+8 = 11 = 11-9 = 2
            return 1+(num-1)%9
        
        """
        # Loop logic
        num = map(int,str(num))
        while len(num) > 1:
            num = map(int,str(sum(num)))
        return num[0]
        """
