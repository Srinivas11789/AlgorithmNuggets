// Day 2
package main

import (
	//"fmt"
	"strings"
	"strconv"
)

func solve2(input []interface{}) (int, int) {

	var day2Inputs []map[string]int

	// Customize input
	for _, val := range input {
		dirAndDist := strings.Split(val.(string), " ")
		distance, err := strconv.Atoi(dirAndDist[1])
		if err != nil { panic(err) }
		day2Inputs = append(day2Inputs, map[string]int{ dirAndDist[0]: distance})
	}

	directions := map[string]int{
		"forward": 1,
		"down": 1,
		"up": -1,
	}

	// Solution 1
	sol1 := 0
	hori := 0
	dept := 0
	for _, i := range day2Inputs {
		for dir, dist := range i {
			if dir == "forward" {
				hori += dist * directions[dir]
			} else {
				dept += dist * directions[dir]
			}
		}
	}
	sol1 = hori * dept

	// Solution 2
	sol2 := 0
	hori = 0
	dept = 0
	aim := 0
	for _, i := range day2Inputs {
		for dir, dist := range i {
			if dir == "forward" {
				hori += dist * directions[dir]
				dept += dist * aim
			} else {
				aim += dist * directions[dir]
			}
		}
	}
	sol2 = hori * dept

	return sol1, sol2
}