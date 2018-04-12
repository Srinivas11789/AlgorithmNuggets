class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        # strstr in c++ is a function that returns the pointer of the first occurrence of str2 in str1 and null pointer if str2 is not in str1
        
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
