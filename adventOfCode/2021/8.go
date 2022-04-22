// Day 8
package main

import (
	//"fmt"
	"strconv"
	"strings"
	mapset "github.com/deckarep/golang-set"
)

func solve8(input []interface{}) (int, int) {

	var day8PrefixDisplay []string
	var day8SuffixDisplay []string
	var day8SuffixDisplayByLine [][]string

	// Customize input
	for _, val := range input {
		outputs := []string{}
		line := strings.Split(val.(string), "|")
		pre := strings.Split(strings.TrimSpace(line[0]), " ")
		for _, p := range pre {
			day8PrefixDisplay = append(day8PrefixDisplay, p)
		}
		suf := strings.Split(strings.TrimSpace(line[1]), " ")
		for _, s := range suf {
			day8SuffixDisplay = append(day8SuffixDisplay, s)
			outputs = append(outputs, s)
		}
		day8SuffixDisplayByLine = append(day8SuffixDisplayByLine, outputs)
	}

	// Solution 1
	sol1 := 0

	// segment displays
	uniqSegmentCombinations := map[int]mapset.Set{
		1: mapset.NewSetFromSlice([]interface{}{"c", "f"}),
		4: mapset.NewSetFromSlice([]interface{}{"b", "c", "d", "f"}),
		7: mapset.NewSetFromSlice([]interface{}{"a", "c", "f"}),
		8: mapset.NewSetFromSlice([]interface{}{"a", "b", "c", "d", "e", "f", "g"}),
	}
	uniqLengths := mapset.NewSetFromSlice([]interface{}{2, 3, 4, 7})

	for _, val := range day8SuffixDisplay {
		for _, uniq := range uniqSegmentCombinations {
			temp := val
			if !uniqLengths.Contains(len(temp)) {
				//fmt.Println(temp)
				continue
			}
			for len(temp) > 0 && uniq.Contains(string(temp[0])) {
				temp = temp[1:]
			}
			if len(temp) == 0 {
				sol1 += 1
				break
			}
		}
	}

	// Solution 2
	sol2 := 0

	// segment displays
	newUniqSegmentCombinations := map[string]mapset.Set{
		"8": mapset.NewSetFromSlice([]interface{}{"a", "c", "e", "d", "g", "f", "b"}),
		"5": mapset.NewSetFromSlice([]interface{}{"c", "d", "f", "b", "e"}),
		"2": mapset.NewSetFromSlice([]interface{}{"g", "c", "d", "f", "a"}),
		"3": mapset.NewSetFromSlice([]interface{}{"f", "b", "c", "d", "a"}),
		"7": mapset.NewSetFromSlice([]interface{}{"d", "b", "a"}),
		"9": mapset.NewSetFromSlice([]interface{}{"c", "e", "f", "d", "a", "b"}),
		"6": mapset.NewSetFromSlice([]interface{}{"c", "e", "f", "d", "g", "b"}),
		"4": mapset.NewSetFromSlice([]interface{}{"a", "e", "f", "b"}),
		"0": mapset.NewSetFromSlice([]interface{}{"c", "a", "g", "e", "d", "b"}),
		"1": mapset.NewSetFromSlice([]interface{}{"a", "b"}),
	}

	/*
	9, 6 --> 6 segments
	8 --> 7 segments
	7 --> 3 segments (top, right: always) --> start with this
	2,3,5 --> 5 segments
	4 --> 4 segments
	1 --> 2 segments

	0. if the line has 7 segments lighted, then its easy --> shld be 8 (use that combo)
	1. if the line has 6 segments lighted, then its also easy to conclude it shld be 9 (use that combo)
	2. if the line has 2,3 segments lghted, then conclude --> abc is 7 (defg is left) ---> [1,7], verify with 
	*/

	for _, stream := range day8SuffixDisplayByLine {
		output := ""
		for _, val := range stream {
			//fmt.Println(val, output)
			for num, uniq := range newUniqSegmentCombinations {
				if len(val) != uniq.Cardinality() {
					continue
				} 
				temp := val
				for len(temp) > 0 && uniq.Contains(string(temp[0])) {
					temp = temp[1:]
				}
				if len(temp) == 0 {
					output += num
					break
				}
			}
		}
		if output == "" {
			continue
		}
		//fmt.Println(output)
		n, err := strconv.Atoi(output)
		if err != nil { panic(err) }
		sol2 += n
	}

	return sol1, sol2
}