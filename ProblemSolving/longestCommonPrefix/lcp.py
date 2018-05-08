class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        # Length of any string would do as it a common prefix
        if not strs:
            return ""
        if "" in strs:
            return ""
        
        n = len(strs[0])

        # Pythonic with indexes
        result = []
        # Should be n+1 to include the total string 
        for i in range(n+1):
            select = None
            count = 0
            for words in strs:
                #print words[:i]
                if select is None:
                    select = words[:i]
                    count += 1
                else:
                    if words[:i] == select:
                        count += 1
            if count == len(strs):
                result.append(select)
        print result
        return result[-1]
            
