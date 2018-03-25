# Codility - Dynamic Programming -- numberSolitaire 

# Exact Solution as the codesays, learn from it -- clean solution
def solution(A):
    # The first six items are used for padding only, so that we can have
    # a unified for loop, no matter how many squares are there in input.
    # The first item is never accessed.
    max_so_far = [A[0]] * (len(A) + 6)
 
    for index in range(1, len(A)):
        # Because we have a fixed length of window as 6, the time
        # complexity of max(max_so_far[index : index + 6]) is O(1).
        max_so_far[index + 6] = max(max_so_far[index : index + 6]) + A[index]
    #print(max_so_far)
    return max_so_far[-1]
