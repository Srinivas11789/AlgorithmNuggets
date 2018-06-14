class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        # Hard code the first 2 rows as a memo
        if numRows == 0:
            return []
        else:
            memo = [[1]]

        # Logic:
        # * Leave out 0 and len()-1
        # * for i add prev(i-1) + prev(i)
        
        while len(memo) < numRows:
            i = 1
            prev = memo[-1]
            memo.append([1])
            while i < len(memo)-1:
                value = prev[i-1]+prev[i]
                memo[-1].append(value)
                i += 1
            memo[-1].append(1)
        return memo
