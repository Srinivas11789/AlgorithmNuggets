# Pending...
# Tree Game

"""
# Tree Structure

	 0
      /  |  \
     0   0   0
    /|  /|\   | \ 
   1 0 4-4 0 -3  0
    /|
   8 0

# Rule:
* Player 1 starts the game
* Player 2 plays alternate chances
* AIM: To maximize the score of player 1 when he ends the game
* Only the leaf nodes contain the score

# Data Inferred:
* Player 1 plays on even level ids of the tree
* Player 2 plays on odd levels
* Player 2 tries to minimize the score as much as possible and player 1 tries to maximize 

# TIP: 
* Boil the score up the tree from the leaf nodes to get the scores of each node
* This is not a BST --- Analyze the tree

"""

class Node:
      
      def __init__(self, value):
          self.value = value
          self.children = []
          

def game(root, score, level):
   
    if not root.value:
       result = []
       for child in root.children:
           result.append(game(child))
       if level%2 == 0:
          score = max(result)
       else:
          score = min(result)
    else:
       return root.value


score = 0
level = 0
game(root, score, level)
