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
        
        # Stack Method
        Slist = list(S)
        # Only round brackets are present
        n = len(Slist)
        result = 0
        i = 0
        while i < n:
            if Slist[i] == ")":
                j = i-1
                while "(" != Slist[j]:
                    j -= 1
                diff = i-j
                if diff == 1:
                    S[j] = 1
                    S.pop(i)
                    i = j - 1
                elif diff == 2:
                    mid = 2*int(S[j+1])
                    S[j] = mid
                    S.pop(j+1)
                    S.pop(j+1)
                    i = j - 1
                else:
                    mid = S[j+1:i]
                    s = 0
                    for m in mid:
                        s += int(m)
                    S[j+1] = s
                    k = j+2
                    while S[k] != ")":
                        S.pop(k)
                    i = j - 1
            print S
        return S
                        
                    
                    
                    
                    
                    
                    
                    
        
            
        
