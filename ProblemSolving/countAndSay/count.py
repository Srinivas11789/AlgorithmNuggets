# Two Pointer Technique - 100 pass
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype:str
        """
        
        # 1 11 21 
        
        total = 1
        start = ["1"]
        
        while total < n:
            
            prev = start[-1]
            init = 0
            move = 1
            ans = ""
            
            while init < len(prev):
                
                current_count = 1
                
                while move < len(prev) and prev[init] == prev[move]:
                    current_count += 1
                    move += 1
                current_count = str(current_count)
                ans += current_count
                ans += prev[init]
                init = move
                move += 1
            start.append(ans)
            total += 1
        
        print start
        return start[-1]
        
        
        """
        i = 1
        memo = [["1"]]
        while i < n:
            current = memo[-1]
            j = 0
            memo.append([])
            count = 1
            # Logic for counting the sequence
            while j < len(current):
                print i,count
                if j == len(current)-1:
                    if current[j] == current[j-1]:
                        count += 1
                    memo[-1].append(str(count)+current[j])
                elif current[j] == current[j+1]:
                    count += 1
                elif current[j] != current[j+1]:
                    memo[-1].append(str(count)+current[j])
                    count = 1
                j += 1
            i += 1
            print memo
        return "".join(memo[-1])
        """
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

"""
# Logic 2: Memoize and Perform the Iteration until length -->100 pass 73% faster
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 0:
            return ""
        memo = ["1"]
        for c in range(1, n+1):
            target = memo[-1]
            word = ""
            i = 0
            while i < len(target):
                ch = target[i]
                j = 1
                i += 1
                while i < len(target) and target[i] == ch:
                    i += 1
                    j += 1
                word += str(j) + ch
            memo.append(word)
        return memo[-2]
"""        
