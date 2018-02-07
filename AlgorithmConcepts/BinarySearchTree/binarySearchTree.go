package main

import "fmt"

type node struct {
	value int
	left *node
	right *node
}

type Tree struct {
        root *node
        size int
}

func insertNode(value int, root node) {
     if root.value == 0 {
        root.value = value
     }
     if value < root.value {
        if root.left == nil {
           root.left = &node{value: value}
	} else {
           insertNode(value, *root.left)
	}
     } else {
        if root.right == nil {
           root.right = &node{value: value}
        } else {
           insertNode(value, *root.right)
        }		
     }
}

func searchNode(value int, root node) node {
     if value < root.value { 
        if root.left == nil {
           return node{}
        } else if root.left.value == value {
           return root
        } else {
           searchNode(value, *root.left)
        }
     } else if value > root.value{
        if root.right == nil {
           return node{}
        } else if root.right.value == value {
           return root
        } else {
           searchNode(value, *root.right)
        }
     } else {
         return root
     }
     return node{}
}

func deleteNode(value int) {

}

func minimum() {

}

func maximum() {

}

func displayTree() {

}

func main() {
     root := node{value: 3}
     Bst := Tree{root: &root}
     Bst.size++
     fmt.Println(Bst.root.value, Bst.root.left, Bst.root.right)
     insertNode(2,Bst.root)
     fmt.Println(Bst.root.value, Bst.root.left, Bst.root.right)
     //insertNode(4,root)
     //insertNode(5,root)
     var search_node = searchNode(2, root)
     fmt.Println(search_node)
}
