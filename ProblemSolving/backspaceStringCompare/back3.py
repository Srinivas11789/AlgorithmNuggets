class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        def removeBackspace(txt):
            stack = []
            for i in txt:
                if i == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(i)
            return "".join(stack)
        
        return removeBackspace(s) == removeBackspace(t)
