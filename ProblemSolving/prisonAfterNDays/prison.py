class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        
        # Naive Method of iteration - with pattern identification
 	# Lesson Learned:
        # * Identify any pattern to reduce iterations
        
        # Identify pattern --> every 14th iteration has same values --> So mod 14 and then bruteforce
        if N > 14:
            N = N%14
        if N == 0:
            N = 14
        
        # Brute force for the answer - Only brute force from the beginning will fail the challenge with 1000000000 input --> will lead to time limit exceeded
        day = 0
        new = cells[:]
        while day < N:
            print(day, new)
            for i in range(1, len(cells)-1):
                if cells[i-1] == cells[i+1]:
                    new[i] = 1
                else:
                    new[i] = 0
            new[0] = 0
            new[len(cells)-1] = 0
            cells = new[:]
            day += 1
        return cells
        
        
        
                
        
