# Logic 1
def parts_sums(array):
    total = sum(array)
    result = [total]
    for item in array:
        total = total-item
        result.append(total)
    return result

# Logic 2
def parts_sums(ls):
    result = [0]
    for item in ls[::-1]:
        result.append(result[-1]+item)
    return result[::-1]
    

