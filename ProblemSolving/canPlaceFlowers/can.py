class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        # Going through too much confusion with respect to the logic. Be clear and innovative. Confused with indices and flowerbed entries.
        
        # Flowerbed length
        l = len(flowerbed)
        
        # While loop for more control
        i = 0
        
        # Result array for indices that are possible, could also use count here.
        indexes = []
        
        # Control loop
        while i < l:
            
            # If one then skip twice to go across the alternative
            if flowerbed[i] == 1:
                
                # Check for previous entry already existing and delete if it does
                if i-1 in indexes:
                    del indexes[len(indexes)-1]
                i += 2
            else:
                
                # Check if previous is zero before appending to indexes
                if i-1 > 0 and i-1 not in indexes:
                    indexes.append(i)
                    
                # Check for i = 0 condition
                elif i == 0:
                    indexes.append(i)
                i += 1
                
        print indexes
        
        # Compare for possibility
        if n <= len(indexes):
            return True
        else:
            return False
                
        
        # Any Alternative Approach
                
            
            
        
            
