class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Logic 1: Recursion
        # Kind of like backtracking, tree of valid paranthesis combinations
        """
        def generate(current, o, c, selected):
            #print(current, selected, o, c)
            if o == c == 0:
                selected.append(current)
                return
            if o > 0:
                generate(current+"(", o-1, c, selected)
            if c > 0 and c > o:
                generate(current+")", o, c-1, selected)
            return selected
        
        # Every N pair can be N of open and close paran
        open_braces = n
        closed_braces = n
        return generate("", open_braces, closed_braces, [])
        """
        
        # Logic 2: Iterative of the same logic
        result = []
        possible_ones = [["", n, n]] # [combination, open, close]
        while possible_ones:
            n = len(possible_ones)
            while n > 0:
                comb, o, c = possible_ones.pop(0)
                if o == c == 0:
                    result.append(comb)
                else:
                    if o > 0:
                        possible_ones.append([comb+"(", o-1, c])
                    if c > 0 and c > o:
                        possible_ones.append([comb+")", o, c-1])
                n -= 1
        return result
