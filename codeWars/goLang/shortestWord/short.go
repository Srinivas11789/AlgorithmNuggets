package kata

import (
    "sort"
    "strings"
    "fmt"
)

// Logic 1
// Using sort by function length 
// * Create a sort interface and define a function to sort by length of items, then return the first element
// Reference: https://gobyexample.com/sorting-by-functions

type byLen []string

func (s byLen) Len() int {
    return len(s)
}

func (s byLen) Swap(i, j int) {
    s[i], s[j] = s[j], s[i]
}

func (s byLen) Less(i, j int) bool {
    return len(s[i]) < len(s[j])
}

func FindShort(s string) int {
    fmt.Println(s)
    words := strings.Split(s, " ")
    fmt.Println(words)
    sort.Sort(byLen(words))
    fmt.Println(words)
    return len(words[0])
}

// Logic 2
// * Iterate over each string and obtain the minimum value
func FindShort(s string) int {
  words := strings.Split(s, " ")
  mini := 9223372036854775807
  for i:=0; i<len(words); i++ {
      if len(words[i]) < mini {
          mini = len(words[i])
      }
  }
  return mini
}
