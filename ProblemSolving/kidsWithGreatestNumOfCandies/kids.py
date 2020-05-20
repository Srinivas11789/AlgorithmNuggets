class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        # Logic 1: Find maximum and iterate the array to construct result - 100 pass 56% - Probably 2*O(N) --> one to find max and other to iterate for result --> O(N)
        greatestNumber = max(candies)
        result = []
        for i in range(len(candies)):
            becomeGreat = False
            if candies[i] + extraCandies >= greatestNumber:
                becomeGreat = True
            result.append(becomeGreat)
        return result

