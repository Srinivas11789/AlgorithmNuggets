// Day 3
package main

import (
	"fmt"
	"strconv"
	mapset "github.com/deckarep/golang-set"
)

func solve3(input []interface{}) (int, int) {

	var day3Inputs []string

	// Customize input
	for _, val := range input {
		if val == "" { continue }
		day3Inputs = append(day3Inputs, val.(string))
	}

	// Solution 1
	sol1 := 0
	n := len(day3Inputs)
	numOnes := []int{}
	gamma := ""
	epilson := ""
	for _, val := range day3Inputs {
		for i := 0; i < len(val); i++ {
			if val[i] == 49 {
				if i >= len(numOnes) {
					numOnes = append(numOnes, 1)
				} else {
					numOnes[i] += 1
				}
			}
		}
	}
	
	for _, i := range numOnes {
		if i >= n/2 {
			gamma += "1"
			epilson += "0"
		} else {
			gamma += "0"
			epilson += "1"
		}
	}

	gammaInt, err := strconv.ParseInt(gamma, 2, 64)
	if err != nil {
		panic(err)
	}
	epilsonInt, err := strconv.ParseInt(epilson, 2, 64)
	if err != nil {
		panic(err)
	}
	sol1 = int(gammaInt * epilsonInt)

	// Solution 2
	sol2 := 0


	oxygen := mapset.NewSet()
	positionZeros, positionOnes := getCounts(day3Inputs)
	var ov, zv mapset.Set
	index := 0

	for oxygen.Cardinality() != 1 {

		ov = positionOnes[index]
		zv = positionZeros[index]
		
		//fmt.Println(index, ov, zv)

		if ov.Cardinality() >= zv.Cardinality() {
			if oxygen.Cardinality() == 0 { 
				oxygen = ov 
			} else { 
				oxygen = oxygen.Intersect(ov) 
			}
		} else {
			if oxygen.Cardinality() == 0 { 
				oxygen = zv 
			} else { oxygen = oxygen.Intersect(zv) }
		}

		// Fail safe
		if oxygen.Cardinality() == 0 {
			fmt.Print("something wrong")
			break
		}
		index += 1
		//fmt.Println("---->", index, oxygen)

		oslice := oxygen.ToSlice()
		var oxy []string
		for _, i := range oslice {
			oxy = append(oxy, i.(string))
		}
		positionZeros, positionOnes  = getCounts(oxy)
	}

    co2 := mapset.NewSet()
	positionZeros, positionOnes = getCounts(day3Inputs)
	index = 0

	for co2.Cardinality() != 1 {

		ov = positionOnes[index]
		zv = positionZeros[index]
		
		//fmt.Println(index, ov, zv)

		if ov.Cardinality() >= zv.Cardinality() {
			if co2.Cardinality() == 0 { 
				co2 = zv
			} else { 
				co2 = co2.Intersect(zv) 
			}
		} else {
			if co2.Cardinality() == 0 { 
				co2 = ov 
			} else { co2 = co2.Intersect(ov) }
		}

		// Fail safe
		if co2.Cardinality() == 0 {
			fmt.Print("something wrong")
			break
		}
		index += 1
		//fmt.Println("---->", index, co2)

		oslice := co2.ToSlice()
		var oxy []string
		for _, i := range oslice {
			oxy = append(oxy, i.(string))
		}
		positionZeros, positionOnes  = getCounts(oxy)
	}
	
	o2, err := strconv.ParseInt(oxygen.Pop().(string), 2, 64)
	if err != nil {
		panic(err)
	}

	c2, err := strconv.ParseInt(co2.Pop().(string), 2, 64)
	if err != nil {
		panic(err)
	}

	sol2 = int(o2*c2)

	return sol1, sol2
}


func getCounts(inputs []string) (map[int]mapset.Set, map[int]mapset.Set) {
	positionOnes := make(map[int]mapset.Set)
	positionZeros := make(map[int]mapset.Set)
	for _, val := range inputs {
		for i := 0; i < len(val); i++ {

			// Add positions 
			if i >= len(positionOnes) {
				positionOnes[i] = mapset.NewSet()
			}
			if i >= len(positionZeros) {
				positionZeros[i] = mapset.NewSet()
			}

			// Add to ones or zeros
			if string(val[i]) == "1" {
				positionOnes[i].Add(val)
			} else {
				positionZeros[i].Add(val)
			}
		}
	}
	return positionZeros, positionOnes
}