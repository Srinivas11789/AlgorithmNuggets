class Solution(object):
    def missingNumber(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        # Logic 2: Reading Q again, we are told that the first and the last position are always correct and there is only one chance of misplacement - 32 ms - 66% faster 
        
        a = arr[0]
        n = len(arr)
        
        # AR formula nth number = a + (n-1)d
        # d = (arr[n] - a)//(n-1)
        if arr[0] < arr[-1]:
            d = (arr[-1] - a)//(n)
            print(a, d)
            for i in range(1, len(arr)):
                ith = arr[i-1] + d
                if arr[i] != ith:
                    return ith
        else:
            d = (arr[-1] - a)//-(n)
            print(a, d)
            for i in range(1, len(arr)):
                ith = arr[i-1] - d
                if arr[i] != ith:
                    return ith
        return 0
        
         
        """
        Logic 1: with dictionary to track diffs - Fail
        
        n = len(arr)
        if arr[n-1] < arr[0]:
            arr = arr[::-1]
        diffs = {}
        maxi = -float('inf')
        d = 0
        removed = 0
        for i in range(1, len(arr)):
            diff = arr[i]-arr[i-1]
            if diff not in diffs:
                diffs[diff] = [0, i]
            diffs[diff][0] += 1
            if diffs[diff][0] > maxi:
                maxi = diffs[diff][0]
                d = diff
        if maxi > -float('inf'):
            removed = arr[diffs[d][1]] + d
        return removed
        """
