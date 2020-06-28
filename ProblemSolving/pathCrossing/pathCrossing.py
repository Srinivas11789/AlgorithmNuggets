class Solution:
    def isPathCrossing(self, path: str) -> bool:
        steps = {"[0, 0]"}
        step = [0,0]
        for p in path:
            if p == "N":
                step[1] += 1
            elif p == "S":
                step[1] -= 1
            elif p == "E":
                step[0] += 1
            else:
                step[0] -= 1
            #print(step, steps)
            if str(step) in steps:
                return True
            steps.add(str(step))
        return False

s = Solution()
print(s.isPathCrossing("NESW"))
