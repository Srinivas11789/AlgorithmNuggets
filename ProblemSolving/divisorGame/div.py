class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        
        def play_game(number):
            
            # Find Divisor
            for i in range(1, (number//2)+1):
                if number%i == 0:
                    # Return the difference
                    return number-i
            return None
        
        count = 0
        while N != None:
            N = play_game(N)
            count += 1
            print count, N
        
        if count%2 != 0:
            return False
        else:
            return True
