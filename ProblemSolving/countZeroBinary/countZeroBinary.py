
#### Codility Problems
## They test the ability to create testcase, write code and performance ---- think think think, after submission you cannot change!!!!!!!!!

### Binary number zero count -> between one's 
### Made mistake in the logic to count between every pair of ones, but when number is like 100100001 or trailing zeros exist like 100100000 the logic failed as every time the other one was hit the pair got over and you reset the value of hit. Changed the logic for it to work. Please veriy all the testcase up to your knowledge and then submit --> eg. 51712, 328, 66561
### 
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    binary = bin(N)[2:]
    #print(binary)
    hit = 0
    max = 0
    count = 0
    for i in range(len(binary)):
        value = int(binary[i])
        #print(value)
        if value == 1:
            if hit == 0:
                hit = 1
            else:
                if count > max:
                    max = count
                #hit = 0
                count = 0
        else:
            count += 1
                    
    return max
            
