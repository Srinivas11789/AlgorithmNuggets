class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        
        # 2*O(N) iteration to consider L and R separately with calculating force
        dominoes = list(dominoes)
        forces = [0]*len(dominoes)
        
        rightPush = False
        curr_f = 0
        for i in range(len(dominoes)):
            
            if rightPush:
                curr_f += 1

            if dominoes[i] == "R":
                rightPush = True
                curr_f = 0
                continue
                
            if rightPush and dominoes[i] == ".":
                dominoes[i] = "R"
            else:
                rightPush = False
                curr_f = 0
            
            forces[i] = curr_f
        
        print(dominoes, forces)
        
        leftPush = False
        curr_f = 0
        for i in range(len(dominoes)-1,-1,-1):
            
            if leftPush:
                curr_f += 1
            
            if dominoes[i] == "L":
                leftPush = True
                curr_f = 0
                continue
                
            if leftPush:
                if forces[i] == curr_f and dominoes[i] == "R":
                    leftPush = False 
                    dominoes[i] = "."
                elif forces[i] < curr_f and dominoes[i] == "R":
                    leftPush = False 
                elif forces[i] > curr_f and dominoes[i] == "R":
                    dominoes[i] = "L"
                    forces[i] = curr_f
                elif dominoes[i] == "." and leftPush:
                    dominoes[i] = "L"
                    forces[i] = curr_f

        print(dominoes, forces)
    
        return "".join(dominoes)
                
            
