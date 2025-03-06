class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        rc = len(grid)

        if rc == 0:
            return []

        cc = len(grid[0])

        elements = [0]*((rc*cc)+1)
        
        for i in range(rc):
            for j in range(cc):
                elements[grid[i][j]] += 1

        twice = []
        noexist = []
        for i in range(1, (rc*cc)+1):
            v = elements[i]
            if v == 2:
                twice.append(i)
            if v == 0:
                noexist.append(i)
        
        return twice + noexist
