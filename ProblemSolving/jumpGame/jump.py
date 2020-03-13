class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Logic 0: Works Best and easy to understand - 75% faster
        # Ref: https://leetcode.com/problems/jump-game/discuss/535541/Python-super-simple-solution-time%3A-O(N)-space-O(1) --> Good One!
        jump_next = 1 # Move index wise to the right
        for i in nums[:-1]: # O(N) Iteration - Omit the last element as we want to reach here and not jumo
            jump_next = max(jump_next-1, i) # Every move reduce the jump_next as we moved to right and then calculate max jump here
            if not jump_next: # Return false if jump becomes 0
                return False
        return True
        
        # Logic 1: BackTrack - You for sure start at index 1 but you can make any jump up until the maximum possible jump to reach the destination - Memory Limit Exceeded ( Almost all passed! - Need optimization )
        self.last_index = len(nums)-1
        self.result = False
        
        def jump(position, jumps, path):
            #print("==>",position, jumps, path, self.last_index)
            if position == self.last_index:
                if not self.result:
                    self.result = True
            if position not in path:
                for current_jump in jumps:
                    nxt = position + current_jump
                    path.add(position)
                    if nxt < len(nums) and nxt not in path:
                        jump(nxt, range(0, nums[nxt]+1), path)
            else:
                return
        
        jump(0, range(0, nums[0]+1), set())
        return self.result
        
        # Logic NA: BackTrack - Understood the question wrong --> Below logic is for all possible ways to jump to the last index
        """
        self.last_index = len(nums)-1
        def jump(nxt, path):
            if nxt == self.last_index:
                if path:
                    return True
                else:
                    return False
            elif (nxt < len(nums) and nums[nxt] == 0) or nxt > self.last_index:
                return False
            else:
                return jump(nxt+nums[nxt], path+[nxt])
        
        for i in range(self.last_index+1):
            if i == self.last_index and i == 0:
                return True
            else:
                if jump(i, []):
                    return True
            
        return False
        """
