# Codility Problem - AbsoluteDistinctValues

# lenerage pythonic set instead of going over for loop
def solution(A):
    return len(set([abs(item) for item in A]))
        
    
