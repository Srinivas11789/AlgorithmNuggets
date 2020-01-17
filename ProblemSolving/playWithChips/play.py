class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        
        # Logic 1: Brute Force Logic: Test cost at every index
        # * There should be a math involved here - Count all the even and odd spaces on both the sides
        # * For a even index --> Ignore all even as the cost is 0, consider only ODD 
        # * For a odd index --> Ignore all odd as the cost is 0, consider only EVEN
        # * at any index until 0 --> num of odd is equal to num of even
        i = 0
        n = len(chips)
        # At i == 0
        left = 0
        n -= 1 # loose the current index number
        if n%2 == 0:
            right = n//2
        else:
            right = n//2+1
        min_cost = left + right
        i += 1
        while i < n:
            print(i ,left, right)
            # LEFT SIDE OF INDEX
            left += 1
            # RIGHT SIDE OF INDEX
            right -= 1
            if left + right < min_cost:
                min_cost = left + right
            i += 1
        return min_cost
