// Day 3
package main

import (
   //"fmt"
	"errors"
	mapset "github.com/deckarep/golang-set/v2"
)

func solve3(input []interface{}) (interface{}, interface{}) {

	var day3Inputs []string

	// Customize input
	for _, val := range input {
		compartments, ok := val.(string)
		if !ok { panic(errors.New("typeCast")) }
		day3Inputs = append(day3Inputs, compartments)
	}

	// score
	scores := map[string]int{}
	currScore := 1
	for i:=97;i<=122;i++ {
		scores[string(rune(i))] = currScore
		currScore++
	}
	for i:=65;i<=90;i++ {
		scores[string(rune(i))] = currScore
		currScore++
	}
	//fmt.Println(scores)

	// Solution 1
	sol1 := 0
	duplicateItems := []string{} //mapset.NewSet[string]()
	allCompItems := []mapset.Set[string]{}
	
	for _, compartments := range day3Inputs {
		visited := mapset.NewSet[string]()
		n := int(float64(len(compartments))/float64(2))
		for len(compartments) > 0 {
			items := mapset.NewSet[string]()
			currCompartment := compartments[:n]
			//fmt.Println(compartments[:n], compartments[n:])
			if len(currCompartment) > 0 {
				compartments = compartments[n:]
			}
			for _, c := range currCompartment {
				char := string(c)
				items.Add(char)
				for _, iterItem := range allCompItems {
					if !visited.Contains(char) && iterItem.Contains(char) {
						visited.Add(char)
						duplicateItems = append(duplicateItems, char)
					}
				}
			}
			//fmt.Println(duplicateItems)
			allCompItems = append(allCompItems, items)
		}
		allCompItems = []mapset.Set[string]{}
	}
	for _, dup := range duplicateItems {
		sol1 += scores[dup]
	}

	// Solution 2
	sol2 := 0
	duplicateItems = []string{} //mapset.NewSet[string]()
	allCompItems = []mapset.Set[string]{}
	
	for i:=0;i<=len(day3Inputs)-3;i=i+3 {
		//fmt.Println(i, i+1, i+2)
		compartments := []string{day3Inputs[i], day3Inputs[i+1], day3Inputs[i+2]}
		visited := mapset.NewSet[string]()
		for len(compartments) > 0 {
			items := mapset.NewSet[string]()
			currCompartment := compartments[0]
			if len(currCompartment) > 0 {
				compartments = compartments[1:]
			}
			for _, c := range currCompartment {
				char := string(c)
				items.Add(char)
				matched := 1 
				for _, iterItem := range allCompItems {
					if iterItem.Contains(char) {
						matched++
					}
				}
				if !visited.Contains(char) && matched == 3 {
					visited.Add(char)
					duplicateItems = append(duplicateItems, char)
				}
			}
			allCompItems = append(allCompItems, items)
		}
		allCompItems = []mapset.Set[string]{}
		//fmt.Println(duplicateItems, i)
	}
	for _, dup := range duplicateItems {
		sol2 += scores[dup]
	}
	return sol1, sol2
}