class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        # All logic below are 100 pass (variation in timing)
        
        # Modified logic 2 with better intelligence - 48%
        # Ref: https://leetcode.com/problems/counting-bits/discuss/248745/c%2B%2B-100-52ms
        
        result = [0]
        remainder = 1
        for i in range(1, num+1):
            # This checkpoints for all 2*remainder which is 2, 4, 8 
            if i == 2*remainder:
                remainder = 2*remainder
            result.append(result[i-remainder]+1)
        return result
        
        # Logic3 - 55% faster - another logic more mathematical
        # Reference: https://leetcode.com/problems/counting-bits/discuss/246572/My-python-solution
        result = [0]*(num+1)
        for i in range(1,num+1):
            result[i] = result[i//2] + i%2
        return result
        
            
        """
        # Logic 2: Fails for 10, 11, 12, 13
        # * Use the design of binary numbers to make it faster
        # * For every even number visited, there is no num of ones change - 2 (010)
        # * For every odd number visited, there is a num of ones change - 3 (011)
        # * Also, at each digit increase from 2, 4, 8 the number of digits in a binary are constant until that number 2 (010, 011), 4 (100, 101, 110, 111), 8 (1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111)
        result = [0, 1]
        remainder = 0
        for i in range(2, num+1):
            if i%2 != 0:
                result.append(result[-1]+1)
            else:
                if remainder == 0:
                    remainder = i
                    result.append(1)
                else:
                    result.append(result[-1])
                print i, result, remainder
            remainder -= 1
        return result
        """
        
        # Logic 1: 100 pass but Only 5% faster
        # * use collections to count
        # * O(N) iteration and binary number calculation for each number visited in a loop...
        """
        import collections
        result = []
        for i in range(num+1):
            counts = collections.Counter(bin(i)[2:])
            if "1" in counts:
                result.append(counts["1"])
            else:
                result.append(0)
        return result
        """
            
        
