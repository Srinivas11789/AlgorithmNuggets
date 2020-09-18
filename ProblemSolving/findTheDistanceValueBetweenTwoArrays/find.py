class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # Naive method of iterations - 100 pass - 40% faster
        result = 0
        for e1 in arr1: # iterate 1st arr
            for e2 in range(len(arr2)): # iterate 2nd arr
                if abs(e1-arr2[e2]) <= d: # check condition and exit on first match
                    break
                if e2 == len(arr2)-1: # If it reached the last then update result
                    result += 1
        return result
    
"""
        # Naive method of iterations - 100 pass - 50% faster
        result = 0
        no_match = False # This is used to check the state of last index element in arr2
        for e1 in arr1: # iterate 1st arr
            for e2 in range(len(arr2)): # iterate 2nd arr
                if abs(e1-arr2[e2]) <= d: # check condition and exit on first match
                    no_match = False
                    break
                no_match = True
            if e2 == len(arr2)-1 and no_match: # If it reached the last then update result
                result += 1
        return result
"""
                
