class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        
        # Logic 1: O(N) Iteration + Type casting - 100 pass - 1008 ms 15% faster
        """
        result = []
        current = ""
        for i in range(len(A)):
            current += str(A[i])
            if int(current,2)%5 == 0:
                result.append(True)
            else:
                result.append(False)
        return result
        """
        
        # Logic 2: O(N) Iteration - 100 pass - 55.83 % faster
        # * I initially used `current = current*10 + A[i]` to append the integers in integer form resp, which failed at some point as the prefix 0 is lost
        # * Multiply by 2 made sense --> Ref: https://leetcode.com/problems/binary-prefix-divisible-by-5/discuss/265601/Detailed-Explanation-using-Modular-Arithmetic-O(n)
        result = []
        current = None
        for i in range(len(A)):
            if current == None:
                current = A[i]
            else:
                current = current*2 + A[i]
            #print(current)
            if current%5 == 0:
                result.append(True)
            else:
                result.append(False)
        return result
        
