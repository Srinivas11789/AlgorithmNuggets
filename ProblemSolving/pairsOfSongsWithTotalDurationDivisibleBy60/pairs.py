class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        
        
        # Mathematically
        # * First Number --> Take modulus of 60 of the first number: t%60 and record the value visited in a counter
        # * Second Number --> Subtract the t%60 from 60 and obtain the remainder (resulting modulus) --> Add the values accordingly
        
        
        # using dict
        # https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/discuss/256738/JavaC%2B%2BPython-Two-Sum-with-K-60
        import collections
        rec = collections.Counter()
        result = 0
        for t in time:
            result += rec[(60-(t%60))%60]
            rec[t%60] += 1
        return result
        
        
        """
        # using array - 100 pass
        # referring to the https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/discuss/257629/Python-5-lines-array-solution
        modulus = [0]*61
        for t in time:
            print t, (60 - t%60) % 60, t%60
            modulus[-1] += modulus[(60 - t%60) % 60]
            modulus[t%60] += 1
        return modulus[-1]     
        """
        
        
        """
        # Traditional 2 loop method - bruteforce --> time limit exceeded obviously....
        n = len(time)
        result = 0
        for i in range(n):
            for j in range(i+1, n):
                if (time[i] + time[j]) % 60 == 0:
                    result += 1
        return result
        """ 
        
