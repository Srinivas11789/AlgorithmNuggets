class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        self.allowed = ["a", "b", "c"]
        self.total = []
        self.n = n

        def backtrack(current, lastInd, totalInd):
            if self.n == len(current):
                self.total.append(current)
                return
            
            if len(current) > self.n:
                return

            for i in range(len(self.allowed)):
                if lastInd == i:
                    continue
                backtrack(current + self.allowed[i], i, totalInd+i)

        
        for i in range(len(self.allowed)):
            backtrack(self.allowed[i], i, i)
        
        print(self.total)
        if k > len(self.total):
            return ""

        return self.total[k-1]
