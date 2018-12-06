class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        
        # From the given array
        # * Get all the 2 digit number arranged in the descending order
        # * Highest delta from 24 would be the maximum hour
        # * Highest delta from 60 would be the maximum minute
        
        # Easy double loop logic
        max_hour = 24
        max_min = 60
        hmax = -1
        Mmax = -1
        A = [str(i) for i in A]
        result = []
        for comb in itertools.permutations(A, r=2):
            result.append(int("".join(comb)))
        result = sorted(result)[::-1]
        for i in range(len(result)):
            item = result[i]
            if (24 - item <= max_hour and item < 24:
                max_hour = 24 - item
                hmax = i
        hmax = 
        
        
        
        """
        # Single loop logic - try it
        import itertools
        max_hour = 24
        max_min = 60
        hmax = -1
        Mmax = -1
        A = [str(i) for i in A]
        for comb in itertools.permutations(A, r=2):
            if (24 - int("".join(comb))) <= max_hour and int("".join(comb)) < 24:
                max_hour = 24 - int("".join(comb))
                hmax = int("".join(comb))
            if 60 - int("".join(comb)) <= max_min and int("".join(comb)) < 60 :
                if len(set(str(hmax)).intersection(set("".join(comb)))) == 0:
                    max_min = 60 - int("".join(comb))
                    Mmax = int("".join(comb))
        print hmax, Mmax
        if hmax == 0 and Mmax == -1:
            return "00:00"
        if hmax != -1 and Mmax != -1:
            if len(str(hmax)) == 1:
                hmax = "0"+str(hmax)
            if len(str(Mmax)) == 1:
                Mmax = "0"+str(Mmax)
            return str(hmax)+":"+str(Mmax)
        else:
            return ""
        """
            
        
