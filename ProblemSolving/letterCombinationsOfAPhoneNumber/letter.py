class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        # define number keys vs alphabets relation with datastructure
        keys = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        # Logic 1: Using itertools - 94% faster
        """
        import itertools
        combs = []
        result = []
        if not digits:
            return []
        for d in digits:
            combs.append(keys[d])
        for cmb in itertools.product(*combs):
            result.append("".join(cmb))
        return result
        """
        
        # Logic 2: Backtrack - 45% faster
        def backtrack(combination, remaining, result):
            if remaining:
                current = remaining[0]
                remaining = remaining[1:]
                if current in keys:
                    for key in keys[current]:
                        backtrack(combination+key, remaining, result)
                return
            else:
                if combination:
                    result.append(combination)
                return
        
        result = []
        backtrack("",  digits, result)
        return result

"""
# Old logic worked out before a year but still works!
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        import itertools
        keys = [['+'],[''],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        select = []
        result = []
        
        for n in digits:
            select.append(keys[int(n)])
    
        if len(select) == 0:
            return []
        
        for comb in itertools.product(*select):
            result.append("".join(comb))
        return result
"""
