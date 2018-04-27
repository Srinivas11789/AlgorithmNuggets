class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        """
        # Nice testcase, simply using split with a space gets defeated
        Input: "                "
        Output: 17
        Expected: 0
        """
        
        if s:
            s = [char for char in s.split(" ") if char]
            return len(s)
        else:
            return 0
        
