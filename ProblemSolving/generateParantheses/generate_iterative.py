class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        if not n:
            return []
        
        self.stack = [["(",n-1,n]]
        self.params = []
        
        def iterative_to_form():
            while self.stack:
                n = len(self.stack)
                while n:
                    current, l, r = self.stack.pop(0)
                    if l > 0:
                        self.stack.append([current+"(",l-1,r])
                    if r > 0 and l < r:
                        self.stack.append([current+")",l,r-1])
                    if l == r == 0:
                        self.params.append(current)
                    n -= 1
                print(self.stack)
            
        iterative_to_form()
        return self.params
