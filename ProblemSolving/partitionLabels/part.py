class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # 
        # 100 pass - Nice and a clear solution of stripping the string into selected and remaining and finding if strictly atmost one existence is satisfied - references from stefanpochmann
         
        # Group present in the string
        group = []
        
        # Until the expiry of the string 
        while S:
        
            # At Most One Character In a Group, so a multiple group should not contains the same character
            i = 1
            while set(S[:i]) & set(S[i:]):
                i += 1
            
            # Appending each group info
            group.append(i)
        
            # Rest of the string removing the corresponding group under consideration
            S = S[i:]
        
        return group
        
        
