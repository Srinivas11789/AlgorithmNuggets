# works but time limit exceeded --> need to cut O(K) in O(NK)
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        def play(curr_index, score):
            #print(curr_index, score, self.memo)
            
            if curr_index in self.memo:
                #print("in",curr_index, score, self.memo)
                return self.memo[curr_index]
            
            if curr_index == len(nums)-1:
                return score
                    
            max_score = -float('inf')
            curr_score = 0
            for i in range(1, k+1):
                #print("here", curr_index+i)
                if curr_index+i >= len(nums):
                    break
                curr_score = play(curr_index+i, nums[curr_index+i])
                if curr_score > max_score:
                    max_score = curr_score
                    
            #print("there", curr_index, max_score)
            self.memo[curr_index] = score+max_score
            return score+max_score
                
        self.memo = {}
        return play(0, nums[0])
