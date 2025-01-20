class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        
        checkRow = [0]*len(mat)
        checkCol = [0]*len(mat[0])

        cacheNums = [[0] * len(mat[0]) for i in range(len(mat))]
        cacheIndices = {}

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                target = mat[i][j]
                if target not in cacheIndices:
                    cacheIndices[target] = []
                cacheIndices[target].append((i,j))

        for i in range(len(arr)):
            c = arr[i]
            for indi in cacheIndices[c]:
                r, c = indi
                checkRow[r] += 1
                checkCol[c] += 1
                if checkRow[r] == len(mat[0]):
                    return i
                if checkCol[c] == len(mat):
                    return i
        return -1


