class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        # Logic 2: finding boundaries
        
        start = end = None
        prev_end = None
        for i in range(len(dominoes)):
            
            # Mark start and end of pushes
            if dominoes[i] == "R":
                if start != None and end == None: # already visited a start
                    #print(start, i, i-start+1)
                    dominoes = dominoes[:start] + "R"*(i-start+1) + dominoes[i+1:]
                    #print(dominoes)
                start = i
            elif dominoes[i] == "L":
                end = i
                
            # Update once you find boundaries
            if start != None and end != None:
                #print(start, end)
                equal_force = (end-start+1)//2
                no_force = (end-start+1)%2
                total_sub = "R"*equal_force 
                if no_force:
                    total_sub += "."
                total_sub += "L"*equal_force
                #print(start, end, total_sub, equal_force, no_force)
                dominoes = dominoes[:start] + total_sub + dominoes[end+1:]
                prev_end = end
                start = end = None
            elif end != None and start == None:
                if prev_end == None:
                    prev_end = 0
                #print("h", prev_end, end)
                dominoes = dominoes[:prev_end] + (end-prev_end)*"L" + dominoes[end:]
                #print(dominoes)
                prev_end = end
                end = None
            elif i == len(dominoes)-1 and start != None and end == None:
                dominoes = dominoes[:start] + "R"*(len(dominoes)-start)
                start = None
                
        
        return dominoes
    
    
        # Things tried...
        
        # Logic 1: 2*O(N) == O(N)
        # * one for right
        # * other for left
        
        """
        ds = list(dominoes) # string cannot be mutated, convert to list 
        push = False
        
        # execute right
        for i in range(len(ds)):
            if ds[i] == "R":
                push = True
            elif ds[i] == "L":
                push = False
            else: # for dot
                if (i+1 < len(ds) and ds[i+1] == "."):
                    if push: # is already pushed
                        ds[i] = "R"
                
        print(ds)
        
        # execute left
        push = False
        for i in range(len(ds)-1, -1, -1):
            if ds[i] == "L":
                push = True
            elif ds[i] == "R": 
                push = False
            else: # for dot
                if (i-1 >= 0 and ds[i-1] == "."): # is already pushed
                    ds[i] = "L"
            i -= 1
            
        return "".join(ds)
        """
        
        # Logic 2: 2 pointer
