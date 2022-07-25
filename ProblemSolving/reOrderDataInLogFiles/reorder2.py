class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        digit_logs = []
        letter_logs = []
        
        while logs:
            curr = logs.pop(0)
            content = curr.split(" ")
            
            if content[1].isdigit():
                digit_logs.append(curr)
                continue
            else:
                itera = len(letter_logs)-1
                iid = content[0]
                content = " ".join(content[1:])
                
                if itera == -1:
                    letter_logs.append(curr)
                    continue
                
                while itera >= 0:
                    target = letter_logs[itera].split(" ")
                    if content == " ".join(target[1:]):
                        if iid > target[0]:
                            break
                    elif content > " ".join(target[1:]):
                        break
                    itera -= 1
                    
                print(itera, len(letter_logs)-1)
                if itera == len(letter_logs)-1:
                    letter_logs.append(curr)
                else:
                    itera += 1
                    letter_logs = letter_logs[:itera] + [curr] + letter_logs[itera:]
                    
        return letter_logs + digit_logs
