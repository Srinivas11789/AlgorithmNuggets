class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        
        count = {}
        n = len(candies)
        divide = n//2
        
        for candy in candies:
            if candy not in count:
                count[candy] = 0
            count[candy] += 1
        
        if len(count.keys()) >= divide:
            return divide
        else:
            return len(count.keys())
        
"""
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        
        import collections
        bgs = len(candies)//2
        candy = collections.Counter(candies)
        #print(candy)
        
        # When kind of candies are as much as of the girls ( half the students )
        if len(candy.keys()) == bgs:
            return bgs
        
        # When there is indifference, then we calculate common candies for the boys, and then for the girls
        for k, v in candy.items():
            while bgs > 0 and candy[k] > 1:
                candy[k] -= 1
                bgs -= 1
            if candy[k] == 0:
                del candy[k]
        #print(candy)
        return len(candy.keys())-bgs
"""
