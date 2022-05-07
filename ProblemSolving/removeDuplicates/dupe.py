class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        # use stack to store the count --> ref sol --> works 100%
        countStack = []

        i = 0
        while i < len(s):

            #print(s, countStack, i)
            if i == 0 or s[i-1] != s[i]:
                countStack.append(1)
            else:
                countStack[-1] += 1
                
                if countStack[-1] == k:
                    countStack.pop()
                    s = s[:i-k+1] + s[i+1:]
                    i -= k
            
            i += 1
                    
        return s
                
        
        """
        # Iteration iterally following the problem statement - 1 --> all pass but time limit exceeded on scale case
        
        hasDups = True
        
        while hasDups:
            
            hasDups = False
            
            current_char = ""
            current_set = 0
            
            i = 0
            while i < len(s)-1:
                
                j = i+1
                current_char = s[i]
                current_set = 1
                
                while j < len(s) and s[j] == current_char:
                    current_set += 1
                    j += 1
                
                if current_set == k:
                    hasDups = True
                    s = s[:i] + s[j:]
                    
                #print(i, current_char, current_set, hasDups, s)
                i += 1
                
            #print("1: ", current_char, current_set, hasDups, s)
                
        return s
        """
        
        """
        # Iteration iterally following the problem statement - 2 (with set and skipping iteration) --> all pass but time limit exceeded on scale case
        
        hasDups = True
        
        while hasDups:
            
            hasDups = False
            
            current_char = ""
            current_set = 0
            
            i = 0
            while i < len(s)-1:
                
                #print(i, k)
                if i+k <= len(s) and len(set(s[i:i+k])) == 1:
                    hasDups = True
                    s = s[:i] + s[i+k:]
                    break
                    
                i += 1
                
            print(s)
            #print("1: ", current_char, current_set, hasDups, s)
                
        return s 
        """
        
        
        # Sliding window --> brainstorm
        """
        self.window = {}
        
        def create_sliding_window(window):
            
            for w in window:
                if w not in self.window:
                    self.window[w] = 0
                self.window[w] += 1
                
        
        
        for i in range(0, len(s), k):
            
            if not self.window:
                create_sliding_window(s[i:i+k])
                
            if len(self.window) > 2:
                continue
            elif len(self.window) == 2:
            else:
            """
        
        
                
            
                    
                
            
