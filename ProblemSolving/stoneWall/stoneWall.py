### Codility Problem - StoneWall - Build Manhattan Skyline

# * Wall with different heights at different places
# Question was quite confusing
# * Idea Outline is to determine and form peaks of buildings with different heights

def solution(H):
    # Stacks to calculate each building
    stack = []
    n = len(H)
    # Blocks to keep track of buildings block count
    blocks = 0
    # Iterate throught the heights
    for h in H:
        # Idea is to extract the block or the building once a new less height block is obtained
        # Wait for a less height than previous height in the stack, if so remove it as a separate building
        while len(stack) != 0 and h < stack[-1]:
            # Block count and pop stack
            stack.pop()
            blocks += 1
        # If the stack is empty or height is greater then a building is being built either from scratch or stacked
        if len(stack) == 0 or h > stack[-1]:
            stack.append(h)
        
        #print(stack)
    
    blocks += len(stack)
    #print(blocks)
    #print(stack)
    
    return blocks
        
        
    
