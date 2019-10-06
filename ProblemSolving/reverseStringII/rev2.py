class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        # Logic 1: O(N) Iteration
        countK = 1
        index = 0
        for i in range(len(s)):
            if i-index == k:
                if countK%2 != 0:
                    s = s[:index] + s[index:i][::-1] + s[i:]
                else:
                    s = s[:index] + s[index:i] + s[i:]
                index = i
                countK += 1
        if countK%2 != 0:
            s = s[:index] + s[index:][::-1]
        return s
