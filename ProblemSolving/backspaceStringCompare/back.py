class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        # Brute force
        def strFormat(S):
            i = 0
            S = list(S)
            while i < len(S):
                if S[i] == "#":
                    if i-1 >= 0:
                        S.pop(i-1)
                        S.pop(i-1)
                        i = i-1
                    else:
                        S.pop(i)  
                else:
                    i += 1
            return "".join(S)
        
        S = strFormat(S)
        T = strFormat(T)
        
        print S,T
        
        if S == T:
            return True
        else:
            return False
            
            
        
