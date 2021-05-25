class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        odd = 1
        final = 0
        n = len(arr)
        for o in range(1, n, 2):
            for i in range(n):
                if i+o > n:
                    break
                #print(arr[i:i+o])
                final += sum(arr[i:i+o])
        if n%2 != 0:
            #print(arr)
            final += sum(arr)
        return final
