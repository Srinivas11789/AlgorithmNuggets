class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        
        # Brute force - for every possible 0 calculate the closest 1
        
        n = len(seats)
        # Loop from left to right updating distance to 1
        temp = None
        for i in range(n):
            if seats[i] == 0:
                if temp != None:
                    seats[i] = i - temp
            else:
                # Index of 1
                temp = i
                seats[temp] = -1
        
        # loop for right to left
        print seats
        temp = None
        #maxi = 0
        for i in range(n-1,-1,-1):
            if seats[i] != -1:
                if temp != None:
                    if temp-i < seats[i] and seats[i] != 0:
                        seats[i] = temp - i
                    elif seats[i] == 0:
                        seats[i] = temp - i
                    #if seats[i] > maxi:
                    #    maxi = seats[i]
            else:
                temp = i
                
        print seats
        
        return max(seats)
        
        
            
                
