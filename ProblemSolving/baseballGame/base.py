class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        
        score = []
        for i in range(len(ops)):
            if ops[i].isdigit():
                score.append(int(ops[i]))
            elif "-" in ops[i] and ops[i][1].isdigit():
                score.append(int(ops[i]))
            elif ops[i] == "+":
                score.append(int(score[-1])+int(score[-2]))
            elif ops[i] == "C":
                score.pop()
            elif ops[i] == "D":
                score.append(2*int(score[-1]))
            #print score
        return sum(score)
                
                
            
            
