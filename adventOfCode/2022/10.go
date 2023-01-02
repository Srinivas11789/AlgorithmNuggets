// Day 10
package main

import (
	"fmt"
	"strconv"
	"errors"
	"strings"
	mapset "github.com/deckarep/golang-set/v2"
)

func printCRT(crt [][]string) {
	fmt.Println("")
	for _, row := range crt {
		fmt.Println(row)
	}
}

func solve10(input []interface{}) (interface{},interface{}) {

	var day10Inputs [][]string

	// Customize input
	for _, val := range input {
		instruction := strings.Split(val.(string), " ")
		if len(instruction) == 0 { panic(errors.New("input error")) }
		day10Inputs = append(day10Inputs, instruction)
	}

	// Solution 1
	sol1 := 0
	cycles := 1
	register := 1
	for _, ins := range day10Inputs {
		if ins[0] == "noop" {
			cycles++
		} else if ins[0] == "addx" {
			num, err := strconv.Atoi(ins[1])
			if err != nil { panic(err) }
		    cycles++
			sol1 += calcStrength(cycles, register)
			cycles++
			register += num
		} else {
			panic(errors.New("improper input"))
		}
		sol1 += calcStrength(cycles, register)
	}

	// Solution 2
	sol2 := [][]string{}
	cycles = 0
	register = 0
	crt := []string{}

	for _, ins := range day10Inputs {
		//fmt.Println(crt, ins)
		if ins[0] == "noop" {
			cycles++
			if len(crt) >= register && len(crt) <= register+2 {
				crt = append(crt, "#")
			} else {
				crt = append(crt, ".")
			}
			crt, sol2, cycles = resetCRT(cycles, crt, sol2)
		} else if ins[0] == "addx" {
			num, err := strconv.Atoi(ins[1])
			if err != nil { panic(err) }
			for i:=0;i<2;i++ {
				cycles = cycles + 1
				if len(crt) >= register && len(crt) <= register+2 {
					crt = append(crt, "#")
				} else {
					crt = append(crt, ".")
				}
				crt, sol2, cycles = resetCRT(cycles, crt, sol2)
			}
			register += num
		} else {
			panic(errors.New("improper input"))
		}
	}
	printCRT(sol2)
	return sol1, 0
}

func resetCRT(cycles int, currCRT []string, sol2 [][]string) ([]string, [][]string, int) {
	strong_signal := mapset.NewSet[int]()
	strong_signal.Add(40)
	strong_signal.Add(80)
	strong_signal.Add(120)
	strong_signal.Add(160)
	strong_signal.Add(200)
	strong_signal.Add(240)
	if strong_signal.Contains(cycles) {
		sol2 = append(sol2, currCRT)
		return []string{}, sol2, 0
	}
	return currCRT, sol2, cycles
}

func calcStrength(cycles int, register int) int {
	strong_signal := mapset.NewSet[int]()
	strong_signal.Add(20)
	strong_signal.Add(60)
	strong_signal.Add(100)
	strong_signal.Add(140)
	strong_signal.Add(180)
	strong_signal.Add(220)
	if strong_signal.Contains(cycles) {
		return cycles * register
	}
	return 0
}