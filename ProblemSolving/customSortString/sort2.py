class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        
        return "".join(sorted(T, key=lambda x: list(S).index(x) if x in S else float('inf')))
