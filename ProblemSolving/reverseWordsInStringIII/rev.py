class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(" ")
        n = len(s)
        for i in range(n):
            s[i] = s[i][::-1]
        return " ".join(s)
