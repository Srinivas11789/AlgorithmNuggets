# Codility Brackets with Strings problem

def solution(S):

    # 100 percent pass
    """
    braces = {'(':')','{':'}','[':']'}
    bracket = []
    n = len(S)
    if n == 0:
        return 1
    for i in range(n):
        if S[i] in braces.keys():
            bracket.append(S[i])
        if S[i] in braces.values():
            if len(bracket) > 0:
                if braces[bracket[len(bracket)-1]] == S[i]:
                    del bracket[len(bracket)-1]
                else:
                    return 0
     ################################################## One test case failed because of below logic missing
     ## * testcase tested was '}}}}' based on past experiences. If the list remains zero and all close braces are present then we got to handle it.
     ## * Lesson: look at different scenarios with different cases, the point of reference is brackets array being filled, question if it is emoty what to do?????
	    else:
                return 0
    if bracket:
        return 0
    else:
        return 1
    """
