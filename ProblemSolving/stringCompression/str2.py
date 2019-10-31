class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        
        # Logic 1: 2 pointer method - inplace replacement is the only way you could do this...
        
        select = 0
        i = 1
        n = len(chars)
        
        length = 1
        
        while i < n:
            
            count = 1
            
            while i < n and chars[i] == chars[select]:
                count += 1
                i += 1
            
            if count > 1:
                count = str(count)
                for dig in count:
                    select += 1
                    chars[select] = dig
                    length += 1
            
            if i < n:
                select += 1
                chars[select] = chars[i]
                length += 1
                i += 1
        
        return length
        
        # Below logic uses extra space
        """
        result = []
        while chars:
            if not result:
                result.append(chars.pop(0))
                result.append("1")
            else:
                if result[-2] == chars[0]:
                    result[-1] = str(int(result[-1])+1)
                else:
                    result.append(chars[0])
                    result.append("1")
                chars.pop(0)
        return len(result)
       """
