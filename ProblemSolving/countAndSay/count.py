# Still working on it -- pending

"""
class Solution(object):    
    
    nums = ["1"]
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        nums = ["0","1"]
        for i in range(2,n+1):
            prev = nums[i-1]
            j = 0
            result = []
            while j < len(prev):
                count = 1
                k = 0
                while j+1 < len(prev) and prev[j] == prev[j+1]:
                    count += 1
                    k += 1
                if j == len(prev)-1:
                    if prev[j] == prev[j-1]:
                        count += 1
                result.append(str(count)+prev[j-1])
                if k > 0:
                    j += k
                else:
                    j += 1
            nums.append("".join(result))
        print nums
        return nums[n]
                    
        
        
        """
        # Recursion logic
        global nums
        if n == 0:
            return nums[0]
        elif nums[n]:
            return nums[n]
        else:
            result = ""
            prev = countAndSay(n-1)
            while i < len(prev):
                count = 0
                while prev[i] == prev[i+1]:
                    count += 1
                    i += 1
                result.append(str(count)+prev[i-1])
            nums.append(result)
            return result
        """
"""             
        
