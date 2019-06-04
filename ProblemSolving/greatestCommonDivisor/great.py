class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        
        
        # Logic2: T + ... + T logic is S
        # * Inconsistent logic fails certain tcs
        """
        n = len(str1)
        m = len(str2)
        
        if n < m:
            divisor = str1
            dividend = str2
        else:
            divisor = str2
            dividend = str1
        
        result = ""
        if divisor in dividend and set(divisor) == set(dividend):
            i = len(divisor)-1 
            while i > 0 and "".join(divisor.split(divisor[:i])) != "": 
                i -= 1
            if i > 0:
                result = divisor[:i]
            else:
                result = divisor
            more = dividend.split(result)
            if len(more) > 1:
                result += more[1]
        return result
        """
        
        # Logic1 <HalfBaked> : Not caring about the order of the substring and the rule
        # * Iterating o(N) to just find common strings
        """
        result = ""
        for i in str1:
            if i in str2:
                if i not in result:
                    result += i
        return result
        """
