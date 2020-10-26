package main

import "fmt"

type node struct {
  data int
  left node
  right node
  parent node
}

func nodes(int value) {
  
}


func insert(node root, node new) {
  if (root == None) {
      return None
  } else if (new.data < root.data) {
      if root.left == None {
         root.left == node
      } else {
         insert(root.left, new)
      } 
  } else if (new.data > root.data) {
      if root.right == None {
         root.right == node
      } else {
         insert(root.right, new)
      }
  }
} 


func main() {
     var root node
     root.data = 3
     insert(root,)
     insert(root, )
     insert(root, )
}


