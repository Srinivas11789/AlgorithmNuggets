class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # 100 pass
        # Logic - Returning the count is enough, no need to pop the array and substitution + required count would work
        # Overwrite the array as we traverse and donot pop or delete anything
        # Reference from user javaleg
        
        n = len(chars)
        
        # as in example 2
        if n <= 1:
            return 1
        
        # 2 pointer technique
        init = 0
        move = 1
        
        total_count = 1
        
        while move < n:
            current_count = 1
            
            # Count the number of similarities
            while move < n and chars[move] == chars[init]:
                move += 1
                current_count += 1
            
            # Count of 1 should be ignored
            if current_count > 1:
                # Count characters should be appened separately
                current_count = str(current_count)
                for ch in current_count:
                    init += 1
                    chars[init] = ch
                    total_count += 1
            
            # The next character
            init += 1
            # Move is at the next diff char
            if move < n:
                chars[init] = chars[move]
                total_count += 1
                move += 1
        
        return total_count
  
        
        """
        i = 0
        select = None
        while i < len(chars):
            if not select:
                select = chars[i]
                index = i
                count = 1
                i += 1
            elif chars[i] == select:
                count += 1
                i += 1
            elif chars[i] != select:
                if count > 1:
                    chars = chars[:index+2]+list(str(count))+chars[i:]
                    select = None
                    i = len(chars[:index+2]+list(str(count)))
                else:
                    select = None
            if i >= len(chars) and count > 1:
                chars = chars[:index+1]+list(str(count))
        
        return len(chars) 
        """
        
        """
        # Compress string with ["Char", "no of times it occured"] - Fails some cases
        # Use O(1) extra space ==> Dictionary method would have been easy, but use 0 space extra
        
        i, count = 0,0
        while i < len(chars):
            count = 2
            select = chars[i]
            if chars[i+1] == select:
                i += 2
                chars[i] = 2
            else:
                i += 1
            while chars[i] == select:
                del chars[i]
                count += 1
                i += 1
        return chars
        """
        
        """
        # Fails large test case
        i, count = 0,0
        index = 0
        ref = 0
        while i < len(chars):
            select = chars[i]
            index = i
            i += 1
            count += 1
            while i < len(chars) and chars[i] == select:
                i += 1
                count += 1
            # Problems might occur here, anticipate and fix
            if count > 1:
                ref = list(str(count))
                del chars[index+len(ref)+1:i]
                chars[index] = select
                for j in range(len(ref)):
                    index += 1
                    chars[index] = ref[j]
                i = index#+len(ref)
                ref = 0
                count = 0
            else:
                count = 0
        """

        """
        i = 0
        count = 0
        select = None
        while i < len(chars):
            #print str(i),select
            if i < len(chars) and select is None:
                print str(i),select, len(chars)
                select = i
                count = 1
                i += 1
                if i == len(chars):
                    return len(chars)
            elif i < len(chars) and chars[i] == chars[select]:
                count += 1
                if not chars[select+1].isdigit(): 
                    chars[select+1] = str(count)
                    i += 1
                elif count > 2:
                        chars[select+1] = str(count)
                        del chars[i]
            else:
                if count > 9:
                    temp = list(str(count))
                    chars = chars[:select+1]+temp+chars[select+len(temp):]
                    i = select+len(temp)+1
                select = None
            if i == len(chars):
                return len(chars)
            print str(i), chars
        #return len(chars)
        """
        
        
        
