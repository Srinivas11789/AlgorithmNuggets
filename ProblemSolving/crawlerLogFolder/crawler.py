class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        level = 0 # at main level
        dir_hierarchy = ["main"] # starting from current directory
        
        while logs:
            
            current_op = logs.pop(0)
            
            if current_op == "../":
                if level > 0:
                    level -= 1
                if len(dir_hierarchy) > 1:
                    dir_hierarchy.pop()
            
            elif current_op == "./":
                continue # remain in the folder means no change in levels
                
            else: # increase level wrt child dir --> no need to check for existence based on info in Q
                
                current_op = current_op.strip("/")
                level += 1
                dir_hierarchy.append(current_op)
            
            print(level, dir_hierarchy)
        
        return level
