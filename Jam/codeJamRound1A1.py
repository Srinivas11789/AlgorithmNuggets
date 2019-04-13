# codeJamRound1A1.py

# Attempt 1 --> Went bruteforce + greedy without taking care of the maximum possibility
# - Sample testcases pass but fails with Wrong answer when submit
"""
def longestSubset(word1, word2):
    n = min(len(word1), len(word2))
    count = 0
    for i in range(1, n+1):
        if word1[-i:] == word2[-i:]:
            count += 1
    return count

def alien_rhymes(words):
    # BruteForce Logic
    n = len(words)
    pairs = []
    count = 0
    for i in range(n):
        for j in range(n):
            if i != j and words[i] not in pairs and words[j] not in pairs:
                if longestSubset(words[i], words[j]) != 0:
                    pairs.append(words[i])
                    pairs.append(words[j])
                    count += longestSubset(words[i], words[j])
                    j = n-1
    return count
                
                

tcs = raw_input()
for i in range(int(tcs)):
    lines = int(raw_input())
    words = []
    for line in range(lines):
        words.append(raw_input())
    print "Case #"+str(i+1)+": "+str(alien_rhymes(words))
"""


# Better logic to maximum the subset length
# Still needs work...
"""
def longestSubset(word1, word2):
    n = min(len(word1), len(word2))
    count = 0
    for i in range(1, n+1):
        if word1[-i:] == word2[-i:]:
            count += 1
    return count

def alien_rhymes(words):
    # BruteForce Logic
    n = len(words)
    pairs = []
    count = 0
    records = {} # Max subset: pair
    # Get all possible combination
    for i in range(n):
        for j in range(n):
            if i != j and words[i]: #not in pairs and words[j] not in pairs:
                subset = longestSubset(words[i], words[j])
                if subset != 0:
                    if subset not in records:
                        records[subset] = (words[i], words[j])
                    else:
                        #while subset in records:
                        #    subset = subset
                        if type(records[subset]) != list:
                            records[subset] = list([records[subset]])
                        records[subset].append((words[i], words[j]))
                    #pairs.append(words[i])
                    #pairs.append(words[j])
                    #count += longestSubset(words[i], words[j])
                    #j = n-1
    subsets = sorted(records.keys(), reverse=True)
    #print records
    for sub in subsets:
        while records[sub]:
            current = records[sub].pop()
            if current[0] not in pairs and current[1] not in pairs:
                count += sub
                pairs.append(current[0])
                pairs.append(current[1]) 
    return count     

tcs = raw_input()
for i in range(int(tcs)):
    lines = int(raw_input())
    words = []
    for line in range(lines):
        words.append(raw_input())
    print "Case #"+str(i+1)+": "+str(alien_rhymes(words))
"""

# codeJamRound1A1.py

# Attempt 1 --> Went bruteforce + greedy without taking care of the maximum possibility
# - Sample testcases pass but fails with Wrong answer when submit
"""
def longestSubset(word1, word2):
    n = min(len(word1), len(word2))
    count = 0
    for i in range(1, n+1):
        if word1[-i:] == word2[-i:]:
            count += 1
    return count

def alien_rhymes(words):
    # BruteForce Logic
    n = len(words)
    pairs = []
    count = 0
    for i in range(n):
        for j in range(n):
            if i != j and words[i] not in pairs and words[j] not in pairs:
                if longestSubset(words[i], words[j]) != 0:
                    pairs.append(words[i])
                    pairs.append(words[j])
                    count += longestSubset(words[i], words[j])
                    j = n-1
    return count
                
                

tcs = raw_input()
for i in range(int(tcs)):
    lines = int(raw_input())
    words = []
    for line in range(lines):
        words.append(raw_input())
    print "Case #"+str(i+1)+": "+str(alien_rhymes(words))
"""

def longestSubset(word1, word2):
    n = min(len(word1), len(word2))
    count = 0
    for i in range(1, n+1):
        if word1[-i:] == word2[-i:]:
            count += 1
    return count

def alien_rhymes(words):
    # BruteForce Logic
    n = len(words)
    pairs = []
    count = 0
    records = {} # Max subset: pair
    weight = {}
    # Get all possible combination
    for i in range(n):
        for j in range(n):
            if i != j and words[i]: #not in pairs and words[j] not in pairs:
                subset = longestSubset(words[i], words[j])
                if subset != 0:
                    if subset not in records:
                        records[subset] = (words[i], words[j])
                    else:
                        #while subset in records:
                        #    subset = subset
                        if type(records[subset]) != list:
                            records[subset] = list([records[subset]])
                        records[subset].append((words[i], words[j]))
                    
                    if (words[i], words[j]) not in weight:
                        weight[(words[i], words[j])] = [subset]
                    else:
                        weight[(words[i], words[j])].append(subset)
                    #pairs.append(words[i])
                    #pairs.append(words[j])
                    #count += longestSubset(words[i], words[j])
                    #j = n-1
    subsets = sorted(records.keys(), reverse=True)
    #print records
    for sub in subsets:
        records[sub] = sorted(records[sub], key=lambda x: len(weight[x]))
        while records[sub]:
            current = records[sub].pop()
            if current[0] not in pairs and current[1] not in pairs:
                count += sub
                pairs.append(current[0])
                pairs.append(current[1]) 
    return count     

tcs = raw_input()
for i in range(int(tcs)):
    lines = int(raw_input())
    words = []
    for line in range(lines):
        words.append(raw_input())
    print "Case #"+str(i+1)+": "+str(alien_rhymes(words))


"""
# Input set
4
2
TARPOL
PROL
3
TARPOR
PROL
TARPRO
6
CODEJAM
JAM
HAM
NALAM
HUM
NOLOM
4
PI
HI
WI
FI

Case #1: 2
Case #2: 0
Case #3: 6
Case #4: 2
"""