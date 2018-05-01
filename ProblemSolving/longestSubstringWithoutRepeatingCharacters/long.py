class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """       
        
        """
        # Solved all cases but time limit exceeded, optimization required
        # As anticipated, the testcase fails when "dvdf"
        # Running along the array, do count for non existing char
        n = len(s)
        count = 0
        select = []
        maxi = 0
        ref = i = 0
        while i < n:
            if select == []:
                select.append(s[i])
                count += 1
                ref = i
                i += 1
            elif s[i] not in select:
                select.append(s[i])
                count += 1
                i += 1
            else:
                select = []
                #select.append(s[i])
                count = 0
                #count += 1
                i = ref+1
            if count > maxi:
                maxi = count
            #print i, ref
        return maxi
        """
        
        """
        # Using python set
        n = len(s)
        maxi = 0
        for i in range(n):
            for j in range(1,n):
                if i+j < n:
                    if s[i:i+j] == set(s[i:i+j]):
                        if len(s[i:i+j]) > maxi:
                            maxi = len(s[i:i+j])
        return maxi
        """
        
        # Optimized - from discussions
        
        # Main reference list to operate on
        select = []
        
        # To hold the maximum
        maxi = 0
        
        # Iterating over the characters work
        for char in s:
            
            # Instead of looking at the character not present, check for the character already present in the list
            if char in select:
                
                # Calculate maximum once the same char is hit again!
                maxi = max(maxi, len(select))
                
                # Removing or Deleting the same character visited and taking into account the remaining part of the array instead of iterating again
                select = select[select.index(char)+1:]
                
            # Append the character under consideration to the list when visited once or visited again
            select.append(char)
            
            #print select
        
        # As we finally added the character to the selected list <after the decision loop>, we have to calculate the maximum again
        maxi = max(maxi, len(select))
        
        return maxi
        
        
        
