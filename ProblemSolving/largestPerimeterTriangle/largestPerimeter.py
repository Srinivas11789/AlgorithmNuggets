class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        # Helper Methods
        
        def validTriangle(sides):
            if (sides[0] + sides[1] > sides[2]) and  (sides[2] + sides[1] > sides[0]) and  (sides[0] + sides[2] > sides[1]):
                return True
            return False
        
        def area(sides):
            # Implement Herons Formula for finding area with sides
            # Reference: https://www.mathopenref.com/heronsformula.html
            import math
            perimeter = sum(sides)
            p = perimeter/2.0
            area = p*(p-sides[0])*(p-sides[1])*(p-sides[2])
            if area > 0:
                return perimeter, True
            else:
                return perimeter, False
            
        
        # Logic 1: Brute force formula with combinations to go over all the combinations - 100 pass but TimeLimitExceeded on last test case
        """
        import itertools
        maxi = 0
        for sides in itertools.combinations(A, r=3):
            if validTriangle(sides):
                perimeter, valid = area(sides)
                if valid:
                    maxi = max(maxi, perimeter)
        return maxi
        """
        
        # Logic 2: Full iteration easier to sort the array of sides and return the first maximum valid triangle - 100 pass but TimeLimitExceeded on last test case
        """
        A = sorted(A, reverse=True)
        maxi = 0
        for i in range(len(A)-2):
            for j in range(i+1, len(A)-1):
                for k in range(j+1, len(A)):
                    sides = [A[i], A[j], A[k]]
                    #print(sides)
                    if validTriangle(sides):
                        perimeter, valid = area(sides)
                        if valid:
                            #maxi = max(maxi, perimeter)
                            return perimeter
        return 0
        """
        
        # Logic 3: Modify the worst case iteration into a single iteration with the sides being next to each other, this wont pass if there occurs combinations of sides that are valid across various ends of the array - 100% pass 97% faster
        
        A = sorted(A, reverse=True)
        maxi = 0
        for i in range(0, len(A)-2):
            sides = [A[i], A[i+1], A[i+2]]
            print(sides)
            if validTriangle(sides):
                perimeter, valid = area(sides)
                if valid:
                    return perimeter
        return 0
        
        
                        
        
        
