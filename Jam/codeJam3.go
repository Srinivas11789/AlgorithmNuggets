package main

import (
	"fmt"
)

func main() {
	var testcases int
	fmt.Scanf("%d", &testcases)
	for i := 0; i < testcases; i++ {
		var N, L int
		fmt.Scanf("%d %d", &N, &L)
		fmt.Println(N, L)
		var ciphertext string
		fmt.Scanf("%s", &ciphertext)
		fmt.Println(ciphertext)
	}
}
