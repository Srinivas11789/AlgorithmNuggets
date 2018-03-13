def ransom_note(magazine, ransom):
    ### Iterative Method
    """
    mag = magazine#[item.lower() for item in magazine]
    ransom = ransom#[item.lower() for item in ransom]
    n = len(ransom)
    match = 0
    for word in ransom:
        if word in mag:
            mag.remove(word)
            match += 1
    if match == n:
        return True
    else:
        return False
    """
    ### Dictionary Method
    mag = {}
    for word in magazine:
        if word not in mag:
            mag[word] = 0
        mag[word] += 1
    for word in ransom:
        if mag[word] == 0 or word not in mag:
            return False
        else:
            mag[word] -= 1
    return True

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
    

