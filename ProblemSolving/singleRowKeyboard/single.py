class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        # Logic 1: Create a dictionary to store the indexes of characters and then calculate the distance after hitting first character 99% faster 
        
        # * Create a dictionary
        alpha = {}
        for i in range(len(keyboard)):
            alpha[keyboard[i]] = i
        
        # * Iterate a find time
        time = 0
        last_index = 0
        for char in word:
            time += abs(alpha[char]-last_index)
            last_index = alpha[char]
        
        return time
        
        
        # Logic 2: Using in built index functionf or list --> 70% faster
        """
        time = 0
        last_index = 0
        for char in word:
            index = keyboard.index(char)
            time += abs(index-last_index)
            last_index = index
        return time
        """
        
        # Logic 3: the alphabets are contiguous A..Z use this to your own idea --> assumption was wrong.... it is not contiguous
        """
        
        # Keyboard has contiguous characters with some shift or any charac of start --> Know the shift first
        
        shift = ord(keyboard[0]) # This would be the start index or start characters ascii value, use this as index 0 for the array
        
        def num_to_char(num):
            while num >= 26:
                num -= 26
            return chr(num)
        
        time = 0
        last_index = 0
        for char in word:
            char_ord = ord(char)-shift
            #print(char_ord, ord(char), shift)
            if char_ord < 0:
                char_ord = 26+char_ord
            time += abs(char_ord-last_index)
            last_index = char_ord
            #if char != keyboard[last_index]:
            print(keyboard[last_index], char, last_index)
        return time
        """
