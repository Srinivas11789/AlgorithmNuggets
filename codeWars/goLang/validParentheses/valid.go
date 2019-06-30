package kata

import (
    "fmt"
)

func ValidParentheses(parens string) bool {
    fmt.Println(parens)
    var stack []string
    for i:=0; i<len(parens); i++ {
        fmt.Println(stack);
        if string(parens[i]) == "(" {
            stack = append(stack, string(parens[i]))
        } else {
            if len(stack) > 0 {
                stack = stack[:len(stack)-1]
            } else {
                return false
            }
        }
    }
    if len(stack) == 0 {
        return true
    } else {
        return false
    }
}
