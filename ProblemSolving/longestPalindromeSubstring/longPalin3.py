class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if not s:
            return ""
        
        self.longest = 1
        self.longest_palin = s[0]
        
        n = len(s)
        possible_palindromes = []
        
        for i in range(0, n-1):
            if i > 0 and s[i-1] == s[i] == s[i+1]:
                possible_palindromes.append((i,"o"))
                possible_palindromes.append((i,"e"))
            elif i > 0 and s[i-1] == s[i+1]:
                possible_palindromes.append((i,"o"))
            elif s[i] == s[i+1]:
                possible_palindromes.append((i,"e"))
                
        m = len(possible_palindromes)
        #print(possible_palindromes)
        
        for i in range(m):
            index, types = possible_palindromes[i]
            if types == "o":
                l = index-1
                h = index+1
            else:
                l = index
                h = index+1
            print(l,h,possible_palindromes[i], s[index])
            target = s[l] == s[h] == s[l-1]
            while l-1 >= 0 and h+1 <= n-1 and s[l-1] == s[h+1]:
                l -= 1
                h += 1
            #print("-->", l,h, possible_palindromes[i], s[l-1], s[h+1])
            if types == "e" and target:
                while l-1 >= 0 and s[l-1] == s[l]:
                    l -= 1
                while h+1 <= n-1 and s[h+1] == s[h]:
                    h += 1
            total = h-l+1
            if  total > self.longest:
                self.longest = total
                print("-->", l,h, possible_palindromes[i])
                self.longest_palin = s[l:h+1]
            
        return self.longest_palin

