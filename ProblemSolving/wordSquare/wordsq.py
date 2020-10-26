class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        # Logic 1: Construct row wise and column wise matrix and then verify equality - 100 pass - 65% faster 
        # 1. row wise arrangement of each word
        matrix = [] # [word.split("") for word in words]
        n = len(words[0])
        for word in words:
            word = list(word)
            matrix.append(word)
            n = max(n, len(word))
        # 2. column wise arrangement of each word ( transpose of a matrix )
        columnwise = [[0 for i in range(len(matrix))] for i in range(n)]
        #print(matrix, columnwise, n)
        for i in range(len(matrix)):
            if len(matrix[i]) < n:
                matrix[i].extend([0]*(n-len(matrix[i])))
            for j in range(n):
                #print(columnwise, matrix, i, j)
                columnwise[j][i] = matrix[i][j]
        if matrix == columnwise:
            return True
        return False
