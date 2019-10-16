class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        prefix = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                prefix += i[0]
            else:
                break
        return prefix
