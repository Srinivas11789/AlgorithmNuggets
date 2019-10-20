class Solution(object):
    def lengthLongestPath(self, inputs):
        """
        :type input: str
        :rtype: int
        """
        
        # Logic 1: Dictionary or Json way of storing stuff
        dirs = {}
        n = len(inputs)
        key = ""
        inputs = list(inputs)
        parents = []
        nest = 0
        maxi = 0
        result = []
        #if n == 1:
        #    return 0
        ws = 0
        while inputs:
            if len(inputs) >= 2 and inputs[0] == "\n":
                inputs.pop(0)
                #if not parents:
                #    parents.append(key)
                if nest:
                    parents = parents[:nest]
                else:
                    parents = []
                nest = 0
                if len(inputs) > 4 and "".join(inputs[:4]) == " "*4:
                    inputs = ["\t"] + inputs[4:]
                    #print("hi")
                while inputs[0] == "\t":
                    inputs.pop(0)
                    nest += 1
                if not nest:
                    key = key.strip()
                parents.append(key)
                key = ""
                ws = 0
            else:
                if inputs[0] == " ":
                    #if key:
                    if nest:
                        key += inputs[0]
                    elif not parents and key:
                        key += inputs[0]
                    #else:
                    #ws += 1
                    inputs.pop(0)
                else:
                    key += inputs.pop(0)
            if not inputs and key:
                if nest:
                    parents = parents[:nest]
                parents.append(key)
            if parents and "." in parents[-1] and len("/".join(parents)) > maxi:
                maxi = len("/".join(parents))
                result = "/".join(parents)
            print(parents, nest, key)
        print(result)
        if ws//4 >= 1:
            ws = ws//4 -1
        else:
            ws = 0
        return len(result)
