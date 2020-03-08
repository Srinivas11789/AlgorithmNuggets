// Logic 2: Repeated same python logic here - 100% faster
import (
    "fmt"
    "strings"
)
func simplifyPath(path string) string {
    stack := []string{}
    elements := strings.Split(path, "/") // Neglect all slahes and add them later
    for _, val := range elements {
        if val == ".." { // Double .. case
            if len(stack) > 0 {
                stack = stack[:len(stack)-1]
            }
        } else if (val == "." || val == "") {
            continue
        } else {
            stack = append(stack, string(val))
        }
    }
    fmt.Println(stack)
    return "/" + strings.Join(stack, "/")
}

/*
// Fail - this does not work - some confusion with the problem statement
import (
    "fmt"
)
func simplifyPath(path string) string {
    var stack string
    for index, value := range path {
        if (len(stack) > 0 && value == '/' && stack[len(stack)-1] == '/') { // Eradicate multiple consecutive slashes
            continue
        } else if ( value == '.' && index+1 < len(path) && path[index+1] == '.') { // Double dot case, pop the last directory
            if (len(stack) > 0 && stack[len(stack)-1] == '/') {
                stack = stack[:len(stack)-1] // remove slash if any
            }
            if len(stack) > 0 {
                stack = stack[:len(stack)-1] // remove the last directory
            }
            index += 1
        } else { // Append everything else that passed allowlist
            if value == '.' {
                   
            } else {
                stack = stack + string(value)
            }
        }
    }
    if (len(stack) > 1) {
        for stack[len(stack)-1] == '/' {
            stack = stack[:len(stack)-1] 
        }
    }
    if len(stack) == 0 {
        stack = string('/')
    }
    return stack
}
*/
