// Day 6
package main

import (
	//"fmt"
	"strconv"
	"strings"
)

func solve6(input []interface{}) (int, int) {

	var laternFishes []int

	// Customize input
	for _, val := range input {
		group := val.(string)
		fishes := strings.Split(group, ",")
		for _, f := range fishes {
			if f == "" { continue }
			fish, err := strconv.Atoi(f)
			if err != nil { panic(err) }
			laternFishes = append(laternFishes, fish)
		}
	}

	// Solution 1
	days := 80
	sol1 := 0
	laternFishesSol1 := make([]int, len(laternFishes))
	copy(laternFishesSol1, laternFishes)

	var currentDayFishes []int
	for day := 0; day < days; day++ {
		currentDayFishes = laternFishesSol1
		for index, fish := range currentDayFishes {
			if fish == 0 {
				laternFishesSol1[index] = 6
				laternFishesSol1 = append(laternFishesSol1, 8)
			} else {
				laternFishesSol1[index] = fish-1
			}
		}
		//fmt.Println(laternFishes)
	}
	/*
		for day < days {
		fmt.Println(day)
		currentDayFishes = laternFishesSol2
		for index, fish := range currentDayFishes {
			if fish-8 <= 0 {
				laternFishesSol2[index] = 6-(8-fish)
				laternFishesSol2 = append(laternFishesSol2, 8)
			} else {
				laternFishesSol2[index] = fish-8
			}
		}
		day += 8
		//fmt.Println(laternFishes)
	}
	*/
	sol1 = len(laternFishesSol1)

	// Solution 2
	days = 256
	sol2 := 0

	laternFishesSol2 := make([]int, len(laternFishes))
	copy(laternFishesSol2, laternFishes)

	var currentDayFishes2 []int

	totalFishes := 0
	childrenAtLevel := make(map[int]int)

	for day := days; day > 0; day-- {
		currentDayFishes2 = laternFishesSol2
		newChildrens := 0
		for index, fish := range currentDayFishes2 {
			if fish == 0 {
				laternFishesSol2[index] = 6
				if _, ok := childrenAtLevel[index]; ok {
					newChildrens += childrenAtLevel[index]
					continue
				}
				newChildrens += 1
			} else {
				laternFishesSol2[index] = fish-1
			}
		}
		//totalFishes += newChildrens*((day-8)/7)
		if newChildrens == 0 { 
			//fmt.Println(laternFishesSol2, days-day)
			continue 
		}
		laternFishesSol2 = append(laternFishesSol2, 8)
		target := len(laternFishesSol2)-1
		if _, ok := childrenAtLevel[target]; !ok {
			childrenAtLevel[target] = 0
		}
		childrenAtLevel[target] += newChildrens
		//fmt.Println(laternFishesSol2, len(childrenAtLevel), days-day)
	}

	for index, _ := range laternFishesSol2 {
		if _, ok := childrenAtLevel[index]; ok {
			totalFishes += childrenAtLevel[index]
			continue
		}
		totalFishes += 1
	}
	//fmt.Println(childrenAtLevel)

	/*
	offspringsByDays := make(map[days]int)
	offspringsByLevel := [][]int

	index := 0
	for len(laternFishesSol2) > 0 {
		currentLevel := laternFishesSol2[0]
		nextLevel := []int{}
		for _, fish := range currentLevel {
			days -= len()
		}
		offspringsByLevel = append(offspringsByLevel, nextLevel)
		laternFishesSol2 = nextLevel
	}

	for index < len(laternFishesSol2) {
		fish := laternFishesSol2[index]
		fmt.Println(index)
		if laternFishesSol2[index] != 8 {
			laternFishesSol2[index] = days-fish
		} else {
			laternFishesSol2[index] = days-8
		}
		offsprings := 1+laternFishesSol2[index]/7
		laternFishesSol2[index] = 7-laternFishesSol2[index]%7
		fmt.Println(fish, laternFishesSol2[index], offsprings)
		for offsprings > 0 {
			laternFishesSol2 = append(laternFishesSol2, 8)
			offsprings -= 1
		}
		//fmt.Println(late 
	}
	*/

	sol2 = totalFishes

	return sol1, sol2
}