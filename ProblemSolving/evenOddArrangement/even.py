# Even to the front of the array and Odd behind the array - with no extra space, operate in the given array
def evenOddArrange(arr):
    odd_index = None
    for i in range(len(arr)):
        if arr[i]%2 == 0:
           if odd_index != None:
              arr[odd_index], arr[i] = arr[i], arr[odd_index]
              odd_index += 1
        else:
           if odd_index == None:
              odd_index = i
    return arr

def main():
    array = [1,2,3,4,5,6,7,8,9]
    print evenOddArrange(array)

main()
