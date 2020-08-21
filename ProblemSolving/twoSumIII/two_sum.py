# Logic 2: 100 pass --> 900ms 10% faster 
# * Compute during find from the diff of numbers added
# * Add to set directly without any ops
class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # arg between set() and dict() here
        # * We need to take care of scenario like 0+0=0 so dict way to get counts
        self.nums = {}
        
    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number not in self.nums:
            self.nums[number] = 1
        else:
            self.nums[number] += 1 
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num, times in self.nums.items():
            other_num = value-num
            # ugly ifs but solves the problem
            if num == other_num and other_num in self.nums: # 1 + 1 = 2
                if times > 1:
                    return True   
            elif value != other_num and other_num in self.nums: # 0 + 0 = 0
                return True
            elif value == other_num and other_num in self.nums: # All other sums
                if times > 1:
                    return True
        return False
        

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

"""
# Logic 1: TIME LIMIT EXCEEDED ( Others pass )
# * Compute during add to maintain a memo of sums
# * Return from set to speed during find
class TwoSum:

    def __init__(self):
        self.nums = []
        self.sums = set()
        
    def add(self, number: int) -> None:
        n = len(self.nums)
        i = 0
        while i < n:
            self.sums.add(self.nums[i]+number)
            i += 1
        self.nums.append(number)
        

    def find(self, value: int) -> bool:
        if value in self.sums:
            return True
        return False
"""
