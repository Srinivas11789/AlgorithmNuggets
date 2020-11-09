# Logic 1: Naive method of O(N) iteration on releastTimes + sort --> 89% faster
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        longest_duration = 0
        keys = []
        
        for r in range(len(releaseTimes)):
            # Calc duration
            if r-1 < 0:
                duration = releaseTimes[r]
            else:
                duration = releaseTimes[r] - releaseTimes[r-1] 
            
            # Assess longest duration
            if duration > longest_duration:
                longest_duration = duration
                keys = [keysPressed[r]]
            elif duration == longest_duration:
                keys.append(keysPressed[r])
            
        keys.sort()
        return keys[-1]
