// Day 5
package main

import (
	"fmt"
	"strconv"
	"strings"
)

func printContainers(stackBuilder [][]string) {
	for _, level := range stackBuilder {
		_ = level[0]
		fmt.Println(level)
	} 
}

func solve5(input []interface{}) (interface{}, interface{}) {

	stackBuilder := [][]string{}
	moves := [][]int{}

	// Read stack from input
	for _, val := range input {
		if strings.Contains(val.(string), "[") {
			currStr := val.(string)
			currLevel := []string{}
			for len(currStr) > 0 {
				current := ""
				if len(currStr) > 4 {
					current = currStr[:4]
					currStr = currStr[4:]
				} else {
					current = currStr[:3]
					currStr = currStr[3:]
				}
				if current == "" {
					continue
				}
				current = strings.TrimSpace(current)
				if current == "" {
					currLevel = append(currLevel, "EE")
					continue
				}
				current = strings.Trim(current, "[]")
				currLevel = append(currLevel, current)
			}
			stackBuilder = append(stackBuilder, currLevel)
		} else {
			break
		}
	}

	// Read moves from Input
	for _, val := range input {
		if strings.Contains(val.(string), "move") {
			curr_move := []int{}
			curr_moves := strings.Split(val.(string), " ")
			for _, c := range curr_moves {
				intVal, err := strconv.Atoi(c)
				if err == nil {
					curr_move = append(curr_move, intVal)
				}
			}
			moves = append(moves, curr_move)
		}
	}	


	// Build stacks
	stacks1 := make([][]string, len(stackBuilder[0]))
	stacks2 := make([][]string, len(stackBuilder[0]))
	for _, level := range stackBuilder {
		for index, value := range level {
			if value != "EE" {
				stacks1[index] = append(stacks1[index], value)
				stacks2[index] = append(stacks2[index], value)
			}
		}
	}

	// Solution 1
	sol1 := ""

	
	for _, m := range moves {
		n := m[0] 
		from := m[1]-1
		to := m[2]-1

		for n > 0 {
			asset := stacks1[from][0]
			if len(stacks1[from]) == 1 {
				stacks1[from] = []string{}
			} else {
				stacks1[from] = stacks1[from][1:]
			}
			stacks1[to] = append([]string{asset}, stacks1[to]...)
			n--
		}
	}

	for _, s := range stacks1 {
		sol1 += s[0]
	}

	
	// Solution 2
	sol2 := ""
	for _, m := range moves {
		n := m[0] 
		from := m[1]-1
		to := m[2]-1

		asset := make([]string, n)
		copy(asset, stacks2[from][:n])
		if len(stacks2[from]) <= n {
			stacks2[from] = []string{}
		} else {
			stacks2[from] = stacks2[from][n:]
		}
		stacks2[to] = append(asset, stacks2[to]...)
	}

	for _, s := range stacks2 {
		sol2 += s[0]
	}

	return sol1, sol2
}