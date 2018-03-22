## Codility Nesting Problem Stacks

def solution(S):
    braces = []
    bracket = {'(':')'}
    for char in S:
        if char in bracket.keys():
            braces.append(char)
        if char in bracket.values():
            if len(braces) > 0:
                if bracket[braces[-1]] == char:
                    del braces[-1]
                else:
                    return 0
            else:
                return 0
    if braces:
        return 0
    else:
        return 1
        
