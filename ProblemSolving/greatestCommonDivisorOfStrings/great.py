class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        def str_div(substring, s1, s2):
            c1 = s1.count(substring)
            c2 = s2.count(substring)
            return substring*c1 == s1 and substring*c2 == s2
        
        if len(str1) < len(str2):
            substr = str1
        else:
            substr = str2
        
        maxi = ""
        for i in range(len(substr)):
            left = substr[:i]
            if left and str_div(left, str1, str2) and len(left) > len(maxi):
                maxi = left
            right = substr[i:]
            if right and str_div(right, str1, str2) and len(right) > len(maxi):
                maxi = right
        return maxi
            
