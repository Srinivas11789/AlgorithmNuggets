// Day 1
package main

import (
	"errors"
	"strconv"
	"strings"
	"unicode"
)

func reverseWord(word string) string {
	r := len(word) - 1
	rev := make([]string, len(word))
	for r >= 0 {
		rev = append(rev, string(word[r]))
		r--
	}
	return strings.Join(rev, "")
}

func d2GetNum(word string, prefixes map[string][]int, words map[string]int) int {
	n := len(word)
	if n == 0 {
		return -1
	}
	lengths, ok := prefixes[string(word[0])]
	if !ok {
		return -1
	}
	for _, l := range lengths {
		if l > n {
			break
		}
		num, ok := words[word[:l]]
		if ok {
			return num
		}
	}
	return -1
}

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
	worded_nums := map[string]int{
		"one":   1,
		"two":   2,
		"three": 3,
		"four":  4,
		"five":  5,
		"six":   6,
		"seven": 7,
		"eight": 8,
		"nine":  9,
	}
	prefixes := map[string][]int{
		"o": []int{3},
		"t": []int{3, 5},
		"f": []int{4},
		"s": []int{3, 5},
		"e": []int{5},
		"n": []int{4},
	}
	for _, word := range day1Inputs {
		var first, last int
		for i, testChr := range word {
			if unicode.IsDigit(testChr) {
				first = int(testChr) - '0'
				break
			}
			first = d2GetNum(word[i:], prefixes, worded_nums)
			if first != -1 {
				break
			}
		}
		n := len(word) - 1
		for n >= 0 {
			testChr := rune(word[n])
			if unicode.IsDigit(testChr) {
				last = int(testChr) - '0'
				break
			}
			last = d2GetNum(word[n:], prefixes, worded_nums)
			if last != -1 {
				break
			}
			n--
		}
		sol2 += (first * 10) + last
	}

	return sol1, sol2
}
