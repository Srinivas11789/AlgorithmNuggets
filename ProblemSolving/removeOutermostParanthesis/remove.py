class Solution(object):
    
    # Logic 1: 100 pass - Balanced brackets check/validation + Paranthesis removal
    # * Only 5 percent faster as the balance check runs every time
    """
    def balanced_or_not(self, exp):
            s = []
            while exp:
                current = exp.pop(0)
                if current == "(":
                    s.append(current)
                else:
                    if s and s[-1] == "(":
                        s.pop()
                    else:
                        return False
            if len(s) == 0:
                return True
            else:
                return False
            
    def removeOuterParentheses(self, S):
        stack = []
        result = ""
        while S:
            current = S[0]
            S = S[1:]
            stack.append(current)
            #print stack
            if self.balanced_or_not(stack[:]):
                    #if stack[1:-1] != "":
                    temp = stack[1:-1]
                    result += "".join(temp)
                    stack = []
            #print stack
        return result
        """
    
    """
    # Logic 2: 100 pass -  Hybrid attempt for the above logic
    def removeOuterParentheses(self, S):
        stack = []
        result = ""
        balanced = False
        temp = ""
        while S:
            current = S[0]
            S = S[1:]
            temp += current
            
            if current == "(":
                stack.append(current)
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            
            if not stack:
                balanced = True
            else:
                balanced = False
                
            if balanced == True:
                    result += temp[1:-1] 
                    stack = []
                    temp = ""
        return result
        """
        
    # Logic 3: 100 pass -  94 - For this problem we are dealing with just the () brackets only and removing just outermost --> Just count the braces
    def removeOuterParentheses(self, S):
            balanced_braces = 0
            result = ""
            temp = ""
            for i in S:
                temp += i
                if i == "(":
                    balanced_braces += 1
                else:
                    balanced_braces -= 1
                #print temp
                if balanced_braces == 0:
                    result += temp[1:-1]
                    temp = ""
            return result
    
        # Counting separate open vs closed braces for a more simpler logic already implemented at https://leetcode.com/problems/remove-outermost-parentheses/discuss/270226/Python-easy-100-solution-with-commentary
                    
        

                        
        
        
        
