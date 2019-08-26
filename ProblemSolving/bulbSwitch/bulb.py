# Still pending...
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # Logic 4:
        # * Taking divisibility test in logic 3 to another level
        # * This solution has interesting math property --> Only perfect squares have odd number of divisibility and only odd leads to bulb being on
        # https://leetcode.com/problems/bulb-switcher/discuss/327486/Python-one-line-solution
        # * Lets do a O(N) iteration instead of a one line solution
        result = 0
        for i in range(int(math.sqrt(n))+1):
            if float(math.sqrt(i+1)).is_integer():
                result += 1
        return result
         
        
        # Logic 3: Divisibility test logic
        """
        def is_divisible(number):
            import math 
            result = 2 # 1 and itself being divisible
            if number == 1:
                return 1
            for i in range(2, (number//2)+1):#int(math.sqrt(number))+1):
                if number%i == 0:
                    result += 1
            return result
        
        switches_with_one = 0
        for i in range(n):
            div_test = is_divisible(i+1)
            #print(i+1, div_test)
            if div_test%2 != 0:
                switches_with_one += 1
        return switches_with_one
        """
        
        # Logic 2: Naive bruteforce
        """
        # Lets assume 1 in ON and 0 is OFF
        # * First steps (1st iteration) also includes constructing the dictionary
        # * So, all are ON
        
        # Initial condition and first round
        switches = [1]*n #[0]*n
        
        # N Rounds with N switches
        for i in range(2, n+1):
            for j in range(i, n+1, i):
                switches[j-1] = switches[j-1]^1
        #print(switches)
        return switches.count(1)
        """
        
        # Logic 1: an attempt before 7 month
        """
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
        """

        
        
        
        
        
