class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        # Corner case of less than zero
        if num == 0:
            return "0"
        
        # Result array to hold the result
        result = []
        
        # Condition handle negative num as we removed the negativity in the first step
        if num < 0:
            result.append("-")
            # remove negativity from num
            num = abs(num)
        else:
            result.append("")
            
        # Convert to base 7 ==> 
        # 1. Add the remainders to result when divided by 7
        # 2. Reduce the number by taking the quotient when dividing by 7
        # Repeat until num becomes zero
        
        while num:
            print num, result
            result.append(str(num%7))
            num = num//7
            
        return result[0]+"".join(result[1:][::-1])
        
        
