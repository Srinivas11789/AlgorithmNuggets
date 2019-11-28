"""
Given a list of words, for each word find the shortest unique prefix. You can assume a word will not be a substring of another word (ie play and playing won't be in the same words list)

Example
Input: ['joma', 'john', 'jack', 'techlead']
Output: ['jom', 'joh', 'ja', 't']
Here's some starter code:

def shortest_unique_prefix(words):
  

print(shortest_unique_prefix(['joma', 'john', 'jack', 'techlead']))
# ['jom', 'joh', 'ja', 't']
"""

def shortest_unique_prefix(words):
  unique_prefix = {}
  visited = set()
  n = len(max(words))
  i = 1
  while i < n:
    w = 0
    while w < len(words):
      if words[w][:i] in visited:
        w += 1
      elif words[w][:i] not in unique_prefix:
        unique_prefix[words[w][:i]] = words[w]
        words.pop(w)
      else:
        words.append(unique_prefix[words[w][:i]]) 
        del unique_prefix[words[w][:i]]
        visited.add(words[w][:i])
        w += 1
      #print(i, words, unique_prefix)
    i += 1
  return unique_prefix.keys()

print(shortest_unique_prefix(['joma', 'john', 'jack', 'techlead']))
# ['jom', 'joh', 'ja', 't']
