class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        
        # Logic 1: Using extra space, a dictionary to hold repeated elements of the array - 100 pass 68 % faster
        """
        import collections
        counter = collections.Counter(arr1)
        result = []
        for element in arr2:
            result.extend([element]*counter[element])
            del counter[element]
        for element in sorted(counter.keys()):
            result.extend([element]*counter[element])
        return result
        """
        
        # Logic 2: Using sorted with custom function - 100 pass 28 % faster
        # * Custom function == relative ordering of array 2 else maximum element plus the element to arrange them in ascending after the arr2 elements
        return sorted(arr1, key=lambda x: arr2.index(x) if x in arr2 else max(arr2)+x)
        
        # Logic 3: Naive Methid with some trick - Using sets - 43 % faster
        # * We already know that array 2 is the correct order
        # * Assume result to be array 2 itself. We just have to arrange the elements that are not in array2 in ascending order 
        result = arr2
        return result + sorted(set(arr2) ^ set(arr1))
