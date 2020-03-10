class Solution(object):
    def reverseString(self, s, i=0, j=-1):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        if i >= len(s)//2:
            return
        s[i], s[j] = s[j], s[i]
        #print(s, i, j)
        self.reverseString(s, i+1, j-1)
        
