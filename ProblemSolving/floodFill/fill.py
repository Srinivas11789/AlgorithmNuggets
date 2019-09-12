class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        # Logic 1: Iterative approach - 93% faster
        """
        # Stack to keep track of the affected pixel
        stack = [[sr, sc]] # initialize with the first pixel
        visited = [] # Keep track of visied pixel to not revisit again
        
        # dimensions
        n = len(image)
        m = len(image[0])
        
        # Iterate until all the pixels have been flooded
        while stack:
            print(stack)
            # Current pixel for consideration
            current = stack.pop(0)
            visited.append(current)
            
            # Add all the affected pixels
            # Top Row
            if current[0]-1 >= 0:
                index = [current[0]-1, current[1]]
                if index not in visited and image[index[0]][index[1]] == image[current[0]][current[1]]:
                    stack.append(index)
            # Botton Row
            if current[0]+1 < n:
                index = [current[0]+1, current[1]]
                if index not in visited and image[index[0]][index[1]] == image[current[0]][current[1]]:
                    stack.append(index)
            # Left Column
            if current[1]-1 >= 0:
                index = [current[0], current[1]-1]
                if index not in visited and image[index[0]][index[1]] == image[current[0]][current[1]]:
                    stack.append(index)
            # Right Column
            if current[1]+1 < m:
                index = [current[0], current[1]+1]
                if index not in visited and image[index[0]][index[1]] == image[current[0]][current[1]]:
                    stack.append(index)
                
            # Alter color of the current pixel
            image[current[0]][current[1]] = newColor
        
        return image
        """
        
        # Logic 2: Recursive approach - 99% faster 
    
        # Recursive Helper Function    
        def fill_pixel(i, j):
            image[i][j] = newColor
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < n and 0 <= y < m and image[x][y] == original:
                    fill_pixel(x, y)
            
        # dimensions
        n = len(image) # Rows
        m = len(image[0]) # Columns
        original = image[sr][sc] # Original Color
        if original != newColor:
            fill_pixel(sr, sc)
        return image

