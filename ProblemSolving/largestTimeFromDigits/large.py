class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        # Logic: I was using permutations from before, but happened to try to reduce the num of iterations
        # * This logic would iterate through the full permutation list everytime
        # * Reference: https://leetcode.com/problems/largest-time-for-given-digits/discuss/211540/Python-simple-obvious-solution
        
        # Get all permutations as usual, store in reverse order to get max hour and corresponding minute
        import itertools
        all_perm = sorted([i for i in itertools.permutations(A, r=4)], reverse=True)
        
        # Iterate through all permutations
        for perm in all_perm:

            # Max hour being first 2 and corresponding minute being the last 2
            hour = str(perm[0])+str(perm[1])
            minute = str(perm[2])+str(perm[3])
            
            # Check for aprropriate hour and minute
            if int(hour) < 24 and int(minute) < 60:
                return hour+":"+minute
        
        # Return for null cases
        return ""
        
        """
        # Convert list to dictionary for faster lookup
        import collections
        As = collections.Counter(A)
        
        time = ""
        
        # To find the max hours, Iterating backwards for max hours
        for i in range(23,-1,-1):
            if len(str(i)) == 1:
                i = str("0")+str(i)
            else:
                i = str(i)
            # Hour found
            if int(i[0]) in As and int(i[1]) in As:
                print i, As
                if (i[0] == i[1] and As[int(i[0])] > 1) or i[0] != i[1]: 
                    time = i
                    if As[int(i[0])] > 1:
                        As[int(i[0])] -= 1
                    else:
                        del As[int(i[0])]
                    if As[int(i[1])] > 1:
                        As[int(i[1])] -= 1
                    else:
                        del As[int(i[1])]
                    break
                    
        
        if time == "":
            return ""
        
        print time, As
        time += ":"
        minute = As.keys()
        
        if len(minute) == 1:
            minute = str(minute[0])*2
            if int(minute) > 59:
                return ""
            time += minute
        else:
            minute = max(int(str(minute[0])+str(minute[1])), int(str(minute[1])+str(minute[0])))
            if minute > 59:
                minute = str(minute)[::-1]
                if int(minute) > 59:
                    return ""
            time += str(minute)

        return time
        """
            
"""
class Solution(object):
    def largestTimeFromDigits(self, A):
        # :type A: List[int]
        # :rtype: str

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
            
        
