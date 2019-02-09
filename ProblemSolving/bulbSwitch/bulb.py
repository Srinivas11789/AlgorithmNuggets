# Pending...

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        
	# Time Limit Exceeded Solution
        import collections
        
        # Lets assume 1 in ON and 0 is OFF
        # * First steps (1st iteration) also includes constructing the dictionary
        # * So, all are ON
        switches = collections.Counter(range(1,n+1))
        
        for i in range(2, n+1):
            if i == 2:
                for k in range(i, n+1, i):
                    switches[k] = 0
            else:
                for k in range(i, n+1, i):
                    switches[k] = switches[k]^1

        return sum(switches.values())
