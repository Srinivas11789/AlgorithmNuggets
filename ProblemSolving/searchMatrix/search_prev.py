class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        selected_col = 0
        selected = False
        row = 0
        for col in range(len(matrix[0])):
            if matrix[row][col] > target:
                selected_col = col-1
                selected = True
                break
            elif matrix[row][col] == target:
                return True
        #print(col)
        if not selected:
            selected_col = col
        print(selected_col)
        while selected_col >= 0:
            for row in range(len(matrix)):
                print(matrix[row][selected_col], selected_col)
                if matrix[row][selected_col] == target:
                    return True
                #elif matrix[row][selected_col] > target:
                #    return False
            selected_col -= 1
        return False
