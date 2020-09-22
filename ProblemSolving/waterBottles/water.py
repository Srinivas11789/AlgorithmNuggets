class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        
        # Logic 1: Use div/modulo of numExchange to loop - lt easy - 100 pass - 20% faster
        result = 0
        while numBottles >= numExchange:
            result += numBottles//numExchange * numExchange
            numBottles = numBottles//numExchange + numBottles%numExchange
            #print(numBottles, result)
        return result + numBottles
