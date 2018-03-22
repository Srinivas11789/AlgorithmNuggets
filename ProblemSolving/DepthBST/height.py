# Codility - Height of a binary search tree

from extratypes import Tree  # library with types used in the task

def solution(T):
        #print(T.x,T.l,T.r)
        if T is None:
            # Important when you do recursion is to properly handle the values according to the scenario. Returning 0 here would give improper results while returning -1 would be the correct solution
            return -1
        else:
            return 1+max(solution(T.l),solution(T.r))

    
    
