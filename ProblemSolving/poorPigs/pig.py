class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        """
        * iterating with T=1 times and 2 Pigs ==> 2^n
        * iterating with T=2 times and 2 Pigs ==> 3^n
        * therefore, (T+1)^N will give T times to test for N pigs to find the poison 
        """
        
        # Number of buckets = n
        # Pig death time = m min 
        # Amount of pigs = x 
        # Time to find out = t min
        # Formula: (1+T)^N 
        
        pigs = 0
        total_times = (minutesToTest/minutesToDie) + 1
        while (total_times)**pigs < buckets:
                pigs += 1
        return pigs
