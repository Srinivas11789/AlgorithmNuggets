class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        # Logic 1: String manipulation --> 59ms faster than 13.8%
        """
        def popChar(s):
            if len(s) > 1:
                s = s[1:]
            else:
                s = ""
            return s
        
        def finalTypedStr(typedStr):
            
            finalStr = ""
            
            while typedStr:
                
                print(typedStr, finalStr)
                if typedStr[0] == "#":
                    if finalStr:
                        finalStr = finalStr[:-1]
                    typedStr = popChar(typedStr)
                    continue
                
                finalStr += typedStr[0]
                
                typedStr = popChar(typedStr)
            
            return finalStr
        
        print(finalTypedStr(s), finalTypedStr(t))
        return finalTypedStr(s) == finalTypedStr(t)
        """
    
        # Logic 2: Stack with single iteration containing 2 pointers -> 46ms faster than 40.5
        
        def typeChrInEditor(char, editorStack):  
            if char == "#":
                if editorStack:
                    editorStack.pop()
            else:
                editorStack.append(char)
        
        s1 = s2 = 0
        stack1 = []
        stack2 = []
        
        while s1 < len(s) or s2 < len(t):
                
            if s1 < len(s):
                typeChrInEditor(s[s1], stack1)
                s1 += 1
                
            if s2 < len(t):
                typeChrInEditor(t[s2], stack2)
                s2 += 1
        
        #print(stack1, stack2)
        if stack1 == stack2:
            return True
        
        return False

