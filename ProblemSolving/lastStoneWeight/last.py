class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        # Logic 1: BruteForce with the sorted function - 22.50% faster
        
        while len(stones) > 1:
            
            # 1. Sort the stones in decreasing order
            stones = sorted(stones, reverse=True)
            
            print stones
        
            # 2. Get the first 2 stones
            first = stones.pop(0)
            second = stones.pop(0)
            
            # 3. Smashing the stones 
            if first == second:
                if 0 not in stones:
                    stones.append(0)
            else:
                stones.append(abs(first-second))
            
            # 4. Reorder the stones again while you enter the loop
            
        return stones[0]
        

        # Different sorted logic?
