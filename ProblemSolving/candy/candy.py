class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        # Logic 1: O(N) iteration 
        n = len(ratings)
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        candies = [1]*n

        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                candies[i] = candies[i-1]+1
        
        min_cost = candies[n-1]
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                v = candies[i+1]+1
                if v > candies[i]:
                    candies[i] = v
            min_cost += candies[i]
            
        #print(candies)
        
        return min_cost
