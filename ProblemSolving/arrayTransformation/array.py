class Solution(object):
    def transformArray(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        # Logic: Lets go naive logic of literally solving - 5.80% faster
        previous = [0]*len(arr)
        new = [1]*len(arr)
        while new != previous:
            previous = new[:]
            new = arr[:]
            for i in range(1,len(arr)-1):
                if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                    new[i] -= 1
                elif arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                    new[i] += 1
            arr = new
            #print(previous, new)
        return previous
