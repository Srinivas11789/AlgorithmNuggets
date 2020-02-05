class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        
        # Logic 1: Naive O(2N) Iteration over the asteroids --> fails for some testcases. Some TCs remain confusing when the adjacent asteroids can be cancelled and are not for example [-2,-2,-2,1] == [-2,-2] as per code below but real answer is [-2,-2,-2,1]
        """
        def collide(asteroids):
            i = 0
            while i < len(asteroids):
                a1 = asteroids[i]
                if i+1 < len(asteroids):
                    a2 = asteroids[i+1]
                else:
                    break
                if a1 > 0 and a2 > 0:
                    i += 2
                    continue
                elif a1 < 0 and a2 < 0:
                    i += 2
                    continue
                else:
                    if abs(a1) == abs(a2):
                        asteroids.pop(i)
                        asteroids.pop(i)
                    else:
                        if abs(a1) > abs(a2):
                            target = a1
                        else:
                            target = a2
                        asteroids.pop(i)
                        if target > 0:
                            asteroids[i] = target
                        else:
                            asteroids.pop(i)
            return asteroids
        
        a = collide(asteroids)
        print(a)
        b = collide(a[::-1])
        return b[::-1]
        """
        
        # Logic 2: Using Stack as mentioned in a number of accepted solutions - 100 pass 68% faster
        stack = []
        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroids[i]):
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(asteroids[i])
                elif stack[-1] == -asteroids[i]:
                    stack.pop()
        return stack
        
                
                
            
                    
