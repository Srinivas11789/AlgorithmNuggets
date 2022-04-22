// Day 7
package main

import (
	//"fmt"
	"strconv"
	"sort"
	"strings"
	"math"
)

var (
	visitedTotal = make(map[int]int)
)

func solve7(input []interface{}) (int, int) {

	var day7Inputs []int

	// Customize input
	for _, val := range input {
		group := val.(string)
		crabs := strings.Split(group, ",")
		for _, c := range crabs {
			if c == "" { continue }
			crab, err := strconv.Atoi(c)
			if err != nil { panic(err) }
			day7Inputs = append(day7Inputs, crab)
		}
	}

	// Solution 1
	sol1 := 0

	visitedOriginFrequency := make(map[int]int)
	var sortedFreqs []int
	var maxFreq int
	var maxPosition int 
	var farthestCrab int

	for _, position := range day7Inputs {

		if position > farthestCrab {
			farthestCrab = position
		}
		if _, ok := visitedOriginFrequency[position]; !ok {
			visitedOriginFrequency[position] = 0
			sortedFreqs = append(sortedFreqs, position)
		}
		visitedOriginFrequency[position] += 1
		if visitedOriginFrequency[position] > maxFreq {
			maxFreq = visitedOriginFrequency[position]
			maxPosition = position
		}
	}

	//fmt.Println(maxFreq, maxPosition)
	//for position, freq := range visitedOriginFrequency {
	//	fmt.Println(position, " ===> ", freq)
	//}

	totalCost := 0
	currentCost := 0

	// (Greedy) Start with highest frequency if there exists one else take midpoint
	if maxFreq > 1 {
		for position, freq := range visitedOriginFrequency {
			currentCost = maxPosition - position
			if currentCost < 0 {
				currentCost *= -1
			}
			totalCost += currentCost * freq
		}
	}

	// (Greedy Bypass) No maxfrequency meaning we use midpoint
	if totalCost == 0 && maxFreq == 1 {
		sort.Ints(sortedFreqs)
		mid := len(sortedFreqs)/2
		midPosition := int(sortedFreqs[mid])
		//fmt.Print(midPosition)
		for position, freq := range visitedOriginFrequency {
			currentCost = midPosition - position
			if currentCost < 0 {
				currentCost *= -1
			}
			totalCost += currentCost * freq
		}
	}

	// (Not doing dynamic) as subproblems dont seem to be related

	// Brute force to ensure all costs
	currCost := 0
	for target, _ := range visitedOriginFrequency {
		currCost = 0
		for position, freq := range visitedOriginFrequency {
			if position == target { continue }
			currentCost = target - position
			if currentCost < 0 {
				currentCost *= -1
			}
			currCost += currentCost * freq
			if currCost > totalCost { // exit for increasing cost
				break
			}
		}
		if currCost < totalCost {
			totalCost = currCost
		}
		//fmt.Println(target, "-->", currCost)
	}

	sol1 = totalCost

	// Solution 2
	sol2 := 0
	totalCost = math.MaxInt

	currCost = 0
	for target:=1;target<farthestCrab;target++ {
		currCost = 0
		for position, freq := range visitedOriginFrequency {
			if position == target { continue }
			currentCost = target - position
			if currentCost < 0 {
				currentCost *= -1
			}
			currentCost = calculateCost(currentCost)
			currCost += currentCost * freq
			if currCost > totalCost { // exit for increasing cost
				break
			}
		}
		if currCost < totalCost {
			totalCost = currCost
		}
		//fmt.Println(target, currCost, totalCost)
		//fmt.Println(target, "-->", currCost)
	}

	//fmt.Println(visitedTotal)

	sol2 = totalCost
	//fmt.Println(visitedTotal)

	return sol1, sol2
}

func calculateCost(diff int) int {
	if diff == 0 {
		return 0
	}
	if _, ok := visitedTotal[diff]; ok {
		return visitedTotal[diff]
	}
	total := diff + calculateCost(diff-1)
	visitedTotal[diff] = total
	return total
}