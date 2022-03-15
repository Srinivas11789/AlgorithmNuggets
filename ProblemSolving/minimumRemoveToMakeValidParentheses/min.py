class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        ends = []
        
        for i in range(len(s)):
            
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    ends.append(i)
                
        #print(stack, ends)
        
        stack.extend(ends)
        result = list(s)
        
        while stack:
            i = stack.pop()
            result[i] = ""
        s = "".join(result)
        
        return s
