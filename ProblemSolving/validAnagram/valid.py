class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        """
        # --- List comparison method: Time Limit Exceeded
        # Anagram validity check
        if len(s) > len(t):
            check = list(s)
            other = list(t)
        else:
            check = list(t)
            other = list(s)
        for char in check:
            if char not in other:
                return False
            else:
                del other[other.index(char)]
        return True
        
        
        # What if unicode characters occur, solution?
        """
        
        """
        # 100pass = To check if same number of elements occur in both the strings
        # Python Hashmap method using collections counter
        sc = collections.Counter(s)
        tc = collections.Counter(t)
        if sc == tc:
            return True
        else:
            return False
        """
        
        """
        # 100 pass - using manual naive hashmap
        sc = {}
        tc = {}
        for char in s:
            if char not in sc:
                sc[char] = 0
            sc[char] += 1
        for char in t:
            if char not in tc:
                tc[char] = 0
            tc[char] += 1
        if sc == tc:
            return True
        else:
            return False
        """
        
        # 100pass = Easy pythonic hack - using sorted both the sides
        if sorted(s) == sorted(t):
            return True
        else:
            return False
        
        
        
        
        
        
