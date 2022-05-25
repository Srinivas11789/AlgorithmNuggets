class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        sl = list(s)
        sl.sort()
        
        result = ""
        #print(sl)
        
        while sl:
            
            i = 0
            inc = ""
            while i < len(sl):
                if inc == "" or (sl and sl[i] != inc[-1]):
                    inc += sl.pop(i)
                else:
                    i += 1
            
            result += inc
            #print(inc)
            
            i = len(sl)-1
            dec = ""
            while i >= 0:
                #print(i, sl)
                if dec == "" or (sl and sl[i] != dec[-1]):
                    dec += sl.pop(i)
                i -= 1      
            
            result += dec
            #print(dec)
            
        return result
            
