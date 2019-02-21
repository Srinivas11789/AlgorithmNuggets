class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        
        # Logic: Divide array by half and navigate correspondingly --> Binary Search Method
        # * rewriting the same logic below in bs
        
        # 2 points for binary navigation
        left = 1
        right = max(piles)
        
        # Iterate until left is equal to right
        while left < right:
            # Mid
            mid = (left + right)//2
            # This was interesting reference: https://leetcode.com/problems/koko-eating-bananas/discuss/152324/C%2B%2BJavaPython-Binary-Search
            # * sometimes I cant use % or // to test the number of times the pile divides like 11//4 which is 3
            # * Add divisor to the pile (subtract 1) to ensure it divides to one lesser and suffices
            if sum((pile+mid-1)//mid for pile in piles) > H:
                left = mid+1
            else:
                right = mid
        return left
        
        # Logic: Bruteforce - going from 2 to max piles fails (reduce the search --> use binary search to divide by half and navigate)
        """
        if len(piles) == H:
            return max(piles)
        elif len(piles) < H:
            for i in range(2, max(piles)):
                if sum(list((pile+i-1)//i for pile in piles)) == H:
                    return i
        else:
            return "Cannot eat when len(piles) > H...!"
        """
        
