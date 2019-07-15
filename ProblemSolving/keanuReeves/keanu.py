# Logic 1
# * Its about finding the minimum number of cuts with all good possible combination
# * Lets go top down (though a dp problem we add a flavour of something similar to greedy) so we get the max and cut remaining to obtain min

# Helper function to decide whether the 2 parts of the string are good or not
def good(word):
    if word == "":
        return False
    import collections
    counts = collections.Counter(word)
    if counts['0'] == counts['1']:
        return False
    else:
        return True

def cuts(n, word, selected):
    # Hold the minimum
    mini = n
    # Handle to choose the selected word based on the minimum
    temp_mini = n
    # Iterate all words (greedy way) from the larger word first
    for i in range(n, 0, -1):
        if good(word[:i]): # the first maximum good substring
            temp_selected = [word[:i]] # Append the first word selected
            m, s = cuts(n-i, word[i:], temp_selected+[word[i:]])
            mini = min(mini, 1+m)
            #print(mini, temp_mini, s, selected)
            if mini < temp_mini:
                selected = s
            #
            print(mini, temp_mini, s, selected)
            temp_mini = mini
    return mini, selected

def cuts2(n, word, words):
    select = list(word)
    for i in range(n, 0, -1):
        if good(word[:i]):
            if not words:
                words = [word[:i]]
            else:
                words.append(word[:i])
            cuts2(n-i, word[i:], words)
            print(word[:i],words, select)
            if len(words) < len(select):
                select = words
                return select
            else:
                break
    return select
                
def main():
    n = int(input())
    string = str(input())
    select = string
    res1 = cuts2(n, string, [])
    print(len(res1))
    for r in res1:
        if r:
            print(r, end=' ')
main()
