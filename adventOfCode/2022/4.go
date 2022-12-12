// Day 4
package main

import (
	//"fmt"
	"strings"
	"strconv"
	"errors"
)

func withinRange(target int, lower int, higher int) bool {
	if lower <= target && target <= higher {
		return true
	}
	return false
}

func solve4(input []interface{}) (interface{}, interface{}) {

	var day4Inputs [][]int

	// Customize input
	for _, val := range input {
		ranges := []int{}
		pairs := strings.Split(val.(string), ",")
		if len(pairs) != 2 {
			panic(errors.New("error"))
		}
		for _, pair := range pairs {
			rnge := strings.Split(pair, "-")
			for _, r := range rnge {
				rint, err := strconv.Atoi(r)
				if err != nil { panic(err) }
				ranges = append(ranges, rint)
			}
		}
		day4Inputs = append(day4Inputs, ranges)
	}

	// Solution 1
	sol1 := 0
	for _, rnge := range day4Inputs {
		lowerElf1, upperElf1 := rnge[0], rnge[1]
		lowerElf2, upperElf2 := rnge[2], rnge[3]
		if withinRange(lowerElf1, lowerElf2, upperElf2) && withinRange(upperElf1, lowerElf2, upperElf2) {
			sol1++
		} else if withinRange(lowerElf2, lowerElf1, upperElf1) && withinRange(upperElf2, lowerElf1, upperElf1) {
			sol1++
		}
	}

	// Solution 2
	sol2 := 0
	for _, rnge := range day4Inputs {
		lowerElf1, upperElf1 := rnge[0], rnge[1]
		lowerElf2, upperElf2 := rnge[2], rnge[3]
		if withinRange(lowerElf1, lowerElf2, upperElf2) || withinRange(upperElf1, lowerElf2, upperElf2) {
			sol2++
		} else if withinRange(lowerElf2, lowerElf1, upperElf1) || withinRange(upperElf2, lowerElf1, upperElf1) {
			sol2++
		}
	}

	return sol1, sol2
}