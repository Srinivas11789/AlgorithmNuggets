class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        letters = [
            [],
            [],
            ["a","b","c"],
            ["d", "e", "f"],
            ["g","h","i"],
            ["j","k","l"],
            ["m","n","o"],
            ["p","q","r","s"],
            ["t","u","v"],
            ["w","x","y","z"]
        ]
        self.result = []
        
        def backtrack(digits, selected):
            
            if not digits:
                self.result.append(selected)
                return
            
            d = digits[0]
            if len(digits) > 1:
                digits = digits[1:]
            else:
                digits = []
                
            current = letters[int(d)]
            
            for l in current:
                backtrack(digits, selected+l)
        
        if not digits:
            return []
        
        backtrack(digits, "")
        return self.result
        
