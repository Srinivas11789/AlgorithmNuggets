// Day 1
package main

import (
	"errors"
	"strconv"
	"unicode"
)

func solve1(input []interface{}) (interface{}, interface{}) {

	var day1Inputs []string

	// Customize input
	for _, val := range input {
		typeVal, ok := val.(string)
		if !ok {
			panic(errors.New("typecast failed"))
		}
		day1Inputs = append(day1Inputs, typeVal)
	}

	// Solution 1
	sol1 := 0
	for _, testStr := range day1Inputs {
		var first, last string
		for _, testChr := range testStr {
			if unicode.IsDigit(testChr) {
				first = string(testChr)
				break
			}
		}
		n := len(testStr) - 1
		for n >= 0 {
			testChr := rune(testStr[n])
			if unicode.IsDigit(testChr) {
				last = string(testChr)
				break
			}
			n--
		}
		totalInt, err := strconv.Atoi(first + last)
		if err != nil {
			return 0, 0
		}
		sol1 += totalInt
	}

	// Solution 2
	sol2 := 0

	return sol1, sol2
}
