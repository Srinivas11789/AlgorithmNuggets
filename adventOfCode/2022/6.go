// Day 6
package main

import (
	//"fmt"
	"errors"
	mapset "github.com/deckarep/golang-set/v2"
)

func procedure(input string, cont int) int {
	window := []string{}
	window_check := mapset.NewSet[string]()
	surpassed_seq := []string{}

	for _, chr := range input {
		charac := string(chr)
		// reset
		if window_check.Contains(charac) {
			for i, val := range window {
				if val == charac {
					if i+1 < len(window) {
						window = window[i+1:]
					} else {
						window = []string{}
					}
					break
				}
			}
			window_check = mapset.NewSet[string]()
			for _, v := range window {
				window_check.Add(v)
			}
		}

		// iterate
		surpassed_seq = append(surpassed_seq, charac)
		window_check.Add(charac)
		window = append(window, charac)

		// exit criteria
		if window_check.Cardinality() == cont {
			return len(surpassed_seq)
		}
	}
	return 0
}

func solve6(input []interface{}) (interface{},interface{}) {

	var day6Inputs []string

	// Customize input
	for _, val := range input {
		sequence, ok := val.(string)
		if !ok { panic(errors.New("panic")) }
		day6Inputs = append(day6Inputs, sequence)
	}

	// Solution 1
	sol1 := 0
	for _, ip := range day6Inputs {
		sol1 = procedure(ip, 4)
	}

	// Solution 2
	sol2 := 0
	for _, ip := range day6Inputs {
		sol2 = procedure(ip, 14)
	}

	return sol1, sol2
}