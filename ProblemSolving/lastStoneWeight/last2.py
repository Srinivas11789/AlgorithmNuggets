class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        while len(stones) > 1:
            print(stones)
            stones = sorted(stones)
            maxi1 = stones[-1]
            maxi2 = stones[-2]
            smash = abs(maxi1 - maxi2)
            stones = stones[:-2]
            if smash:
                stones.append(smash)
        if stones:
            return stones[0]
        else:
            return 0
