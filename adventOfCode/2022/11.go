// Day 11
package main

import (
	"fmt"
	"strings"
	"errors"
	"strconv"
	"math"
	"sort"
)

type monkey struct {
	name int
	items []int
	op string
	opNum int
	divisbleTest int
	throwTrue int
	throwFalse int
	inspectTimes int
}

func printMonkeys(mks []monkey) {
	for j, m := range mks {
		fmt.Printf("\n %d: %+v \n", j, m)
	}
}

func printMonkeyItems(mks []monkey) {
	fmt.Println("\n Items in each monkey are:")
	for j, m := range mks {
		fmt.Println(j, m.items)
	}
}

func solve11(input []interface{}) (interface{},interface{}) {

	var monkeys []monkey

	// Customize input
	currMonkey := monkey{
		inspectTimes: 0,
	}
	for i, val := range input {

		line := val.(string)
		if line == "" {
			monkeys = append(monkeys, currMonkey)
			currMonkey = monkey{
				inspectTimes: 0,
			}
		} else if strings.Contains(line, "items") {
			items := strings.Split(line, ":")
			items = strings.Split(strings.TrimSpace(items[1]), ",")
			for _, it := range items {
				itemNum, err := strconv.Atoi(strings.TrimSpace(it))
				if err != nil { panic(err) }
				currMonkey.items = append(currMonkey.items, itemNum)
			}
		} else if strings.HasPrefix(line, "Monkey") {
			names := strings.Split(line, " ")
			stripName := strings.TrimSuffix(names[1], ":")
			nameNum, err := strconv.Atoi(strings.TrimSpace(stripName))
			if err != nil { panic(err) }
			currMonkey.name = nameNum
		} else if strings.Contains(line, "Test") {
			divs := strings.Split(line, " ")
			divNum, err := strconv.Atoi(strings.TrimSpace(divs[len(divs)-1]))
			if err != nil { panic(err) }
			currMonkey.divisbleTest = divNum
		} else  if strings.Contains(line, "true") {
			monkeyN := strings.Split(line, " ")
			monkeyNum, err := strconv.Atoi(strings.TrimSpace(monkeyN[len(monkeyN)-1]))
			if err != nil { panic(err) }
			currMonkey.throwTrue = monkeyNum
		} else if strings.Contains(line, "false") {
			monkeyN := strings.Split(line, " ")
			monkeyNum, err := strconv.Atoi(strings.TrimSpace(monkeyN[len(monkeyN)-1]))
			if err != nil { panic(err) }
			currMonkey.throwFalse = monkeyNum
		} else if strings.Contains(line, "Operation") {
			line = strings.TrimPrefix(strings.TrimSpace(line), "Operation: new =")
			ops := strings.Split(strings.TrimSpace(line), " ")
			opNum := 0
			if ops[len(ops)-1] != "old" {
				convOp, err := strconv.Atoi(strings.TrimSpace(ops[len(ops)-1]))
				if err != nil { panic(err) }
				opNum = convOp
			}
			currMonkey.opNum = opNum
			currMonkey.op = ops[len(ops)-2]
		} else {
			panic(errors.New("line match failed"))
		}
		if i == len(input)-1 {
			monkeys = append(monkeys, currMonkey)
		}
	}

	// Solution 1
	sol1 := 0
	inspectTimes := make([]int, len(monkeys))

	// 20 rounds
	for r:=0; r < 20 ; r++ {
		for i, m := range monkeys {
			for len(monkeys[i].items) > 0 {
				// 1. Pop the first item
				currItem := monkeys[i].items[0]
				if len(monkeys[i].items) > 0 {
					monkeys[i].items = monkeys[i].items[1:]
				}
				// 2. calculate worry level
				curWorry := calculateWorry(currItem, m.op, m.opNum)

				// 3. round worry level
				round3 := int(math.Floor(float64(curWorry/3)))

				// 4. test logical flow
				if round3 % m.divisbleTest == 0 {
					monkeys[m.throwTrue].items = append(monkeys[m.throwTrue].items, round3)
				} else {
					monkeys[m.throwFalse].items = append(monkeys[m.throwFalse].items, round3)
				}

				monkeys[i].inspectTimes++
				inspectTimes[i] = monkeys[i].inspectTimes
			}
		}
		//printMonkeys(monkeys)
	}
	//printMonkeyItems(monkeys)
	sort.Sort(sort.Reverse(sort.IntSlice(inspectTimes)))
	sol1 = inspectTimes[0] * inspectTimes[1]


	// Solution 2
	sol2 := 0
	inspectTimes = make([]int, len(monkeys))

	// 20 rounds
	for r:=0; r < 10000 ; r++ {
		for i, m := range monkeys {
			for len(monkeys[i].items) > 0 {
				// 1. Pop the first item
				currItem := monkeys[i].items[0]
				if len(monkeys[i].items) > 0 {
					monkeys[i].items = monkeys[i].items[1:]
				}
				// 2. calculate worry level
				curWorry := calculateWorry(currItem, m.op, m.opNum)

				// 3. round worry level
				//round3 := int(math.Floor(float64(float64(curWorry)/2.0)))
				round3 := curWorry
				if round3 > currItem*3 {
					round3 = int(math.Floor(float64(float64(curWorry)/2)))
				}

				// 4. test logical flow
				if round3 % m.divisbleTest == 0 {
					monkeys[m.throwTrue].items = append(monkeys[m.throwTrue].items, round3)
				} else {
					monkeys[m.throwFalse].items = append(monkeys[m.throwFalse].items, round3)
				}

				monkeys[i].inspectTimes++
				inspectTimes[i] = monkeys[i].inspectTimes
			}
		}
		//printMonkeys(monkeys)
	}
	//printMonkeyItems(monkeys)
	sort.Sort(sort.Reverse(sort.IntSlice(inspectTimes)))
	fmt.Println(inspectTimes)
	sol2 = inspectTimes[0] * inspectTimes[1]

	return sol1, sol2
}

func calculateWorry(worry int, op string, opNum int) int {
	if opNum == 0 {
		opNum = worry
	}
	switch op {
	case "*":
		return (worry * opNum)
	case "+":
		return worry + opNum
	case "-":
		return worry - opNum
	case "/":
		return worry / opNum
	}
	return 0
}