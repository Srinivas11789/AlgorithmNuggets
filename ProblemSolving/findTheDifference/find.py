class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        """
        # 100 pass - Simple problem of viewing the unmatched character iterating from a larger list
        # Think of corner cases, when duplicate elements occurs, there occurs problem, solve it well before you think of the solution
        # 100 pass - uses a separate list, try not using a separate list operation
        s = list(s)
        for ch in t:
            if ch not in s:
                return ch
            else:
                del s[s.index(ch)]
        return -1
        """
        
        """
        ### Exor with same char negates itself so combining both the list and exoring each elements will result in the unique element
        ### Using EXOR
        result = 0
        for c in s+t:
            result ^= ord(c)
        return chr(result)
        """
        ### Nice logic - 100 pass
        ### Difference in the sum of hex all the characters 
        s_sum = sum([ord(i) for i in s])
        t_sum = sum([ord(i) for i in t])
        return chr(t_sum-s_sum)
    
        
