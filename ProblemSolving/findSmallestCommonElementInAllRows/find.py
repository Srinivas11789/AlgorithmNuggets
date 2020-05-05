class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        
        # Logic 1: Naive iteration of rows + converting each row into dictionary + finding the frequency of items - 100 pass 6% faster
        import collections
        common = collections.Counter(mat[0])
        for r in range(1, len(mat)):
            rn = collections.Counter(mat[r])
            common = common + rn
            for k,v in common.items():
                if v < r+1:
                    del common[k]
        if common:
            return min(common.keys())
        else:
            return -1

