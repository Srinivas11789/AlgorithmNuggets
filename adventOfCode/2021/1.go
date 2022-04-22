// Day 1
package main

import (
	//"fmt"
	"strconv"
)

func solve1(input []interface{}) (int, int) {

	var day1Inputs []int

	// Customize input
	for _, val := range input {
		integer, err := strconv.Atoi(val.(string))
		if err != nil { panic(err) }
		day1Inputs = append(day1Inputs, integer)
	}

	// Solution 1
	sol1 := 0
	for i, val := range day1Inputs {
		if i == 0 { continue }
		if val <= day1Inputs[i-1] {
			continue
		}
		sol1 += 1
	}

	// Solution 2
	sol2 := 0
	curr_window := 0
	last_window := 0
	for i, _ := range day1Inputs {
		if i+2 >= len(day1Inputs) {
			continue
		}
		curr_window = day1Inputs[i] + day1Inputs[i+1] + day1Inputs[i+2]
		if last_window == 0 {
			last_window = curr_window
		} else if curr_window > last_window {
				sol2 += 1
		}
		last_window = curr_window
	}
	return sol1, sol2
}