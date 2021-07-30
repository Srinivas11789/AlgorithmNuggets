"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        pointer = 0
        start = end = 0
        while n:
            start = pointer
            current_buf = [0]*4
            current_read = read4(current_buf)
            if current_read == 0:
                break
            next_end = end + current_read
            print(start,end,n)
            j = 0
            for i in range(start,next_end):
                buf[i] = current_buf[j]
                j += 1
                n -= 1
                end += 1
                if n == 0:
                    return end
            end = next_end
            pointer = next_end
            print(n,start,end,buf)
        return end
        
        
