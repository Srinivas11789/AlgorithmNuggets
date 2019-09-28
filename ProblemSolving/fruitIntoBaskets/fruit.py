class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        basket1 = 0
        b1type = None
        b1i = 0
        basket2 = 0
        b2type = None
        b2i = 0
        
        max_basket = 0
        
        f = 0
        while f < len(tree):
            if b1type == None:
                b1type = tree[f]
                b1i = f
            elif b2type == None and b1type != tree[f]:
                b2type = tree[f]
                b2i = f
                
            if tree[f] == b1type:
                basket1 += 1
                f += 1
            elif tree[f] == b2type:
                basket2 += 1
                f += 1
            else:
                b1type = None
                b2type = None
                basket1 = basket2 = 0
                f = b2i
            
            max_basket = max(max_basket, basket1+basket2)
            #print(b1type, b2type, basket1, basket2)
            
        return max_basket
                
        
