/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

import (
    "fmt"
)

func middleNode(head *ListNode) *ListNode {
    
    // Logic 1: 2*O(N) iteration over linked list - First for length and next for finding middle
    first := head // for 1st iteration
    second := head // for 2nd iteration
    length := 0
    for first != nil {
        length += 1
        first = first.Next
    }
    middle := length/2
    fmt.Println(middle)
    length = 0
    for second != nil {
        if length == middle {
            return second
        }
        length += 1
        second = second.Next
    }
    return nil
}
