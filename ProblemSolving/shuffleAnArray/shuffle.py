class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.array = nums
        self.mixup = self.array[:]
        self.length = len(self.array)
        
        """
        # Logic2
        # combinations
        import itertools
        self.combinations = []
        for comb in itertools.permutations(self.array[:], r=len(nums)):
            self.combinations.append(comb)
        self.length = len(self.combinations)
        """

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.mixup = self.array[:]
        return self.mixup

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """

        # Logic 1
        import random
        if self.length > 0:
            for i in range(self.length):
                v = random.randint(0, self.length-1)
                self.mixup[v], self.mixup[i] = self.mixup[i], self.mixup[v]
        return self.mixup
        
        #while self.mixup[:] == self.array[:]:
        # self.mixup = self.mixup[v:]+self.mixup[:v] # Not enough randomness
        
        """
        # Logic 2
        if self.length > 0:
            import random
            v = random.randint(0, self.length-1)
            self.mixup = self.combinations[v][:]
        return self.mixup
        """



# Your Solution object will be instantiated and called as such:
#nums = [1,2,3]
#obj = Solution(nums)
#param_1 = obj.reset()
#param_2 = obj.shuffle()
#print param_1
#print param_2
