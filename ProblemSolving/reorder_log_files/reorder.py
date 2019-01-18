class Solution(object):
    # 100 pass logic with the tie checker implemented
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        
        # A log ==> "yy xx xx xx"
        # yy == id
        # xx xx xx == log
        
        # Dictionary to hold all the entries
        # * Digit, store as list to maintain the order
        # * Letters, store as dictionary of id as value, so it is easy to sort the logs vs ids
        dictionary = {
            "letter":{},
            "digit":[]
        }
        
        # Result list
        result = []
        
        # iterate through the logs to fill the dictionary
        # * Digit logs - store with index
        # * Letter logs - store only identifier as keys
        
        for log in logs:
            current_log = log.split(" ")
            # Digit logic - if log contains digit
            if ("".join(current_log[1:])).isdigit():
                dictionary["digit"].append(log)
            else:
                # Store logs as key and id as value
                # Tie checker
                if " ".join(current_log[1:]) not in dictionary["letter"]:
                    dictionary["letter"][" ".join(current_log[1:])] = current_log[0]
                else:
                    # Tie occurred
                    dictionary["letter"][" ".join(current_log[1:])] = [dictionary["letter"][" ".join(current_log[1:])]]
                    dictionary["letter"][" ".join(current_log[1:])].append(current_log[0])
                
        # lexi sort the letter logs without ids
        letter_logs = sorted(dictionary["letter"].keys())
        
        # Logic works without the underlying block - this block checks sorting in the case of a tie and sorts
        # Append letter logs
        for letter in letter_logs:
                # Handle tie condition
                if type(dictionary["letter"][letter]) is list:
                    identifiers = sorted(dictionary["letter"][letter])
                    for i in identifiers:
                        result.append(i+" "+letter)
                
                else:
                    result.append(dictionary["letter"][letter]+" "+letter)
        
        # Append the digit logs in the same order
        result.extend(dictionary["digit"])
        
        return result

    # Another Logic ---> 
    # This logic is 100 pass for this problem without the tie checker implemented....
    def reorderLogFilesWithoutTieCheck(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        
        # Dictionary to hold all the entries
        dictionary = {
            "letter":{},
            "digit":[]
        }
        
        result = []
        
        # iterate through the logs to fill the dictionary
        # * Digit logs - store with index
        # * Letter logs - store only identifier as keys
        
        for log in logs:
            current_log = log.split(" ")
            # Digit logic
            if ("".join(current_log[1:])).isdigit():
                dictionary["digit"].append(log)
            else:
                dictionary["letter"][" ".join(current_log[1:])] = current_log[0]
                
        # lexi sort
        letter_logs = sorted(dictionary["letter"].keys())
        
        for letter in letter_logs:
            result.append(dictionary["letter"][letter]+" "+letter)
        
        result.extend(dictionary["digit"])
        
        return result
