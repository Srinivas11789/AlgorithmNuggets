class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        
        # Logic1: Use SET intersections --> 98% faster 
        """
        return sorted(set(arr1).intersection(arr2).intersection(arr3))
        """
        
        # Logic2: Using SET 'and' functionality --> 86% faster
        """
        return sorted(set(arr1) & set(arr2) & set(arr3))
        """
        
        # Logic3: Using COLLECTIONS (dictionary) in Python --> 30% faster
        """
        return sorted(collections.Counter(arr1) & collections.Counter(arr2) & collections.Counter(arr3))
        """
        
        # Logic4: Using naive/only dictionary + iteration method - 51% faster
        """
        counter = {}
        result = []
        for element in (arr1 + arr2 + arr3):
            if element not in counter:
                counter[element] = 0
            counter[element] += 1
            if counter[element] == 3:
                result.append(element)
        return result
        """
        
        # Logic5: Using iteration ( naive method ) --> Attempted not working
        """
        def get_element(array, index):
            if index > len(array):
                return None
            else:
                return array[index]
        
        i = j = k = 0
        result = []
        
        while 1:
            while arr1[i] != arr2[j] != arr3[k]:
                while arr1[i] < arr2[j]:
                    i += 1
                while arr2[j] < arr3[k]:
                    j += 1
                while arr3[k] < arr1[i]:
                    k += 1
                print(arr1[i], arr2[j], arr3[k])
            result.append(arr1[i])
            i += 1
            j += 1
            k += 1
        """
        
        
            
