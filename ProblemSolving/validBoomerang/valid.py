class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        
        # Logic: Using theorem math formula of collinarity
        # Reference: http://mathworld.wolfram.com/Collinear.html
        # Formula: x_1(y_2-y_3)+x_2(y_3-y_1)+x_3(y_1-y_2)=0
        # * Set is always 3 points as questions says, hence the formula would be an apt match
        
        proof = points[0][0]*(points[1][1]-points[2][1]) + points[1][0]*(points[2][1]-points[0][1]) + points[2][0]*(points[0][1]-points[1][1])
        if proof == 0:
            return False
        else:
            return True
        
        """
        # Brute force 
        # * Some initiative to breaking collinearity
        
        n = len(points)
        delta1 = None
        delta2 = None
        for i in range(n-1):
            p1 = points[i]
            p2 = points[i+1]
            if not delta1 and not delta2:
                delta1 = p2[0] - p1[0]
                delta2 = p2[1] - p1[0]
            else:
                while p1[0]+delta1 < p2[0]:
                    p1[0] += 1
                while p1[1]+delta2 < p2[1]:
                    p1[1] += 1 
                print p1[0], p1[1]
                if p1[0]+delta1 != p2[0] or p1[1]+delta2 != p2[1]:
                    return True
        return False
        """
            
