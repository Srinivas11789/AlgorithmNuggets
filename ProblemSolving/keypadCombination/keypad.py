

"""
Key pad and combinations
"""

def keypadCombinations(num):

    # ds with keys are (relationship datastructure)
    keys = [['+'],[''],['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]

    # total combination
    total = 1
    for item in num:
        total = total * len(keys[item])


    # results list
    result = []

    # Iterate through the numbers enetered
    for i in range(len(num)):

        # calculate corresponding combintion
        total = total // len(keys[num[i]])

        # Initially creating the result array with first characters
        if i == 0:
            for item in keys[num[i]]:
                result.extend(item*total)
        else:
            # Updateing the combinations and iterating over the array to fill
            k = 0
            while k < len(result):
                for item in keys[num[i]]:
                    #value = [item] * total
                    c = 0
                    while c < total:
                        result[k] = result[k] + item
                        c += 1
                        k += 1
    print result



def main():
    num = [2,3,4,0]
    keypadCombinations(num)

main()
