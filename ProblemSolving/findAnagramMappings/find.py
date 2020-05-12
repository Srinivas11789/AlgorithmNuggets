class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        
        # Logic 1: Using dictionary to store indexes in B - 2*O(N) --> 37.87% faster 100 pass
        # 1. iterate over B to create a map - account for duplicates with a list
        # 2. iterate over A to generate results
        mapB = {} # element: [indexes]
        for i in range(len(B)):
            if B[i] not in mapB:
                mapB[B[i]] = []
            mapB[B[i]].append(i)
        result = []
        for element in A:
            result.append(mapB[element].pop())
        return result
