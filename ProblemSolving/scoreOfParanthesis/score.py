class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        
        """
        # Pythonic Method -- Regex -- Fragile Method prone to breaking
        import re
        brac = 0
        ABs = 0
        As = 0
        while len(S) > 1:
            S = S.replace("()","1")
            # AB Condition
            Abs = re.search("([1-9]+2)",S)
            if Abs and Abs.group(1):
                Abs = Abs.group(1).split(1)
                ans = int(Abs[0])+int(Abs[1])
                S = re.sub("[1-9]+2",str(ans),S)
            # A Condition
            As = re.search(r"\(([0-9])\)",S)
            if As and As.group(1):
                As = As.group(1)
                ans = 2*int(As)
                S = re.sub("\([0-9]\)",str(ans),S)
            print S
            nums = re.search(r"([0-9]+)",S)
            #print nums.group(1)
            if nums and nums.group(1):
                ss = nums.group(1)
                r = 0
                for c in ss: 
                    r += int(c)
                S = re.sub("[0-9]+",str(r),S)
        return int(S)
        """
        
        # Stack Method - 100 pass
        
        # String iterator
        Slist = list(S)
        # stack
        stack = []
        
        # Only round brackets are present so no need for a dictionary
        
        # Control variables
        n = len(Slist)
        result = 0
        i = 0
        
        while i < n:
            print i
            if Slist[i] == ")":
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                elif type(stack[-1]) is int and stack[-2] == "(":
                    num = stack.pop()
                    stack.pop()
                    stack.append(num*2)
                else:
                    sumi = stack.pop()
                    while type(stack[-1]) is int:
                        sumi += stack.pop()
                    stack.pop()
                    stack.append(2*sumi)
            else:
                stack.append(Slist[i])
            print stack
            i += 1
                
        return sum(stack)
                        
                    
                    
                    
                    
                    
                    
                    
        
            
        
