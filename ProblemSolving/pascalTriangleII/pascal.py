class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        # Hard code the first 2 rows as a memo
        memo = [[1], [1,1]]

        # Logic:
        # * Leave out 0 and len()-1
        # * for i add prev(i-1) + prev(i)
        
        while len(memo) <= rowIndex:
            i = 1
            prev = memo[-1]
            memo.append([1])
            while i < len(memo)-1:
                value = prev[i-1]+prev[i]
                memo[-1].append(value)
                i += 1
            memo[-1].append(1)
        return memo[rowIndex]
