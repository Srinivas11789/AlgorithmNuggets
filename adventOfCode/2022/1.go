// Day 1
package main

import (
	"sort"
	"strconv"
	"errors"
)

func solve1(input []interface{}) (interface{}, interface{}) {

	var day1Inputs []int

	// Customize input
	for _, val := range input {
		typeVal, ok := val.(string)
		if !ok {
			panic(errors.New("typecast failed"))
		}
		if typeVal == "" {
			day1Inputs = append(day1Inputs, -1)
			continue
		}
		integer, err := strconv.Atoi(typeVal)
		if err != nil { 
			panic(err) 
		}
		day1Inputs = append(day1Inputs, integer)
	}

	// Solution 1
	caloriesPerElf := make([]int, len(day1Inputs))
	sol1 := 0
	currentElfCarrying := 0
	for _, calorie := range day1Inputs {
		if calorie == -1 {
			caloriesPerElf = append(caloriesPerElf, currentElfCarrying)
			if currentElfCarrying > sol1 {
				sol1 = currentElfCarrying
			}
			currentElfCarrying = 0
			continue
		}
		currentElfCarrying += calorie
	}

	// Solution 2
	sol2 := 0
	sort.Ints(caloriesPerElf)
	sol2 += caloriesPerElf[len(caloriesPerElf)-1]
	sol2 += caloriesPerElf[len(caloriesPerElf)-2]
	sol2 += caloriesPerElf[len(caloriesPerElf)-3]

	return sol1, sol2
}