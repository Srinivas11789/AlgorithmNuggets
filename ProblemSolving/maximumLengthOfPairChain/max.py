class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        
        # Logic 1: Naive iteration at every index - O(n**2)
        # Logic 2: Sort with b < c logic and then find the longest
        """
        def custom(p1, p2):
            if p1[1] <= p2[0]:
                return 0
            else:
                return -1
        
        p = sorted(pairs, cmp=custom)
        print(p)
        i = 0
        count = 0
        maxi = 0
        while i+1 < len(p):
            if custom(p[i], p[i+1]):
                print(p[i], p[i+1], count)
                count += 1
            else:
                maxi = max(maxi, count)
                count = 0
                i -= 1
            i += 1
        maxi = max(maxi, count)
        return maxi
        """
        
        # Logic 3: Sort by pair[1] so its arranged accordingly and then iterate - 57% faster
        # Ref: https://leetcode.com/problems/maximum-length-of-pair-chain/discuss/105607/4-Liner-Python-Greedy
        order = sorted(pairs, key=lambda x: x[1])
        current, result = -float('inf'), 0
        for o in order:
            if current < o[0]:
                current = o[1]
                result += 1
        return result
            

