# Given a file, finding the number of particular words in it and print respective results

import collections

def countWords(content):
    results = {}
    # O(1) logic
    for word in content:
        word = word.strip(".?!,;")
        if word not in results:
           results[word] = 0
        results[word] += 1
    max = sorted(results.keys(), reverse=True)
    sort = collections.Counter(results)
    return sort.most_common(10)
    

def main():
    ### Read file logic
    filename = input("Enter the filename:")
    handle = open(filename, 'r')
    content = handle.read().split(" ").strip(".?!,")

def test():
    content = "The man sprang from his chair and paced up and down the room in uncontrollable agitation. Then, with a gesture of desperation, he tore the mask from his face and hurled it upon the ground.You are right, he cried; I am the King. Why?"
    for item in countWords(content.split(" ")):
        print item

test()
   
