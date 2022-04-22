// Day 5
package main

import (
	"fmt"
	"strings"
	"strconv"
	mapset "github.com/deckarep/golang-set"
)

func strToInt(num string) int {
	n, err := strconv.Atoi(num)
	if err != nil {
		panic(err)
	}
	return n
}
 
func solve5(input []interface{}) (int, int) {

	var day5Inputs [][][]string

	// Customize input
	for _, val := range input {
		ranges := strings.Split(val.(string), "->")
		lower := strings.Split(strings.TrimSpace(ranges[0]), ",")
		upper := strings.Split(strings.TrimSpace(ranges[1]),",")
		curr_range := [][]string{lower, upper}
		day5Inputs = append(day5Inputs, curr_range)
	}

	// Solution 1
	sol1 := 0

	allPoints := make(map[string]int)
	overLappedPoints := mapset.NewSet()

	for _, r := range day5Inputs {
		l_x := strToInt(r[0][0])
		l_y := strToInt(r[0][1])
		u_x := strToInt(r[1][0])
		u_y := strToInt(r[1][1])

		var ll, uu int
		if l_x == u_x {
			if l_y > u_y {
				ll = u_y
				uu = l_y
			} else {
				ll = l_y
				uu = u_y
			}
			for i:=ll;i<uu+1;i++ {
				curr_point := strconv.Itoa(l_x) + "," + strconv.Itoa(i)
				if _, ok := allPoints[curr_point]; !ok {
					allPoints[curr_point] = 0
				}
				allPoints[curr_point] += 1
				if allPoints[curr_point] > 1 {
					overLappedPoints.Add(curr_point)
				}
			}
		} else if l_y == u_y {
			if l_x > u_x {
				ll = u_x
				uu = l_x
			} else {
				ll = l_x
				uu = u_x
			}
			for i:=ll;i<uu+1;i++ {
				curr_point := strconv.Itoa(i) + "," + strconv.Itoa(l_y)
				if _, ok := allPoints[curr_point]; !ok {
					allPoints[curr_point] = 0
				}
				allPoints[curr_point] += 1
				if allPoints[curr_point] > 1 {
					overLappedPoints.Add(curr_point)
				}
			}
		} else {
			//fmt.Println("unhandled situation")
			continue
		}
	}

	//fmt.Println(allPoints, overLappedPoints, overLappedPoints.Cardinality())
    sol1 = overLappedPoints.Cardinality()

	// Solution 2
	sol2 := 0 
	allPoints2 := make(map[string]int)
	overLappedPoints2 := mapset.NewSet()

	for _, r := range day5Inputs {
		l_x := strToInt(r[0][0])
		l_y := strToInt(r[0][1])
		u_x := strToInt(r[1][0])
		u_y := strToInt(r[1][1])

		var ll, uu, lly, uuy int
		if l_x == u_x {
			if l_y > u_y {
				ll = u_y
				uu = l_y
			} else {
				ll = l_y
				uu = u_y
			}
			for i:=ll;i<uu+1;i++ {
				curr_point := strconv.Itoa(l_x) + "," + strconv.Itoa(i)
				if _, ok := allPoints2[curr_point]; !ok {
					allPoints2[curr_point] = 0
				}
				allPoints2[curr_point] += 1
				if allPoints2[curr_point] > 1 {
					overLappedPoints2.Add(curr_point)
				}
			}
		} else if l_y == u_y {
			if l_x > u_x {
				ll = u_x
				uu = l_x
			} else {
				ll = l_x
				uu = u_x
			}
			for i:=ll;i<uu+1;i++ {
				curr_point := strconv.Itoa(i) + "," + strconv.Itoa(l_y)
				if _, ok := allPoints2[curr_point]; !ok {
					allPoints2[curr_point] = 0
				}
				allPoints2[curr_point] += 1
				if allPoints2[curr_point] > 1 {
					overLappedPoints2.Add(curr_point)
				}
			}
		} else {
			if l_x > u_x {
				ll = u_x
				uu = l_x
				lly = u_y
				uuy = l_y
			} else {
				ll = l_x
				uu = u_x
				lly = l_y
				uuy = u_y
			}
			target := strconv.Itoa(uu) + "," + strconv.Itoa(uuy)
			diff := 0
			curr_points := mapset.NewSet()
			if ll <= uu && lly <= uuy {
				for ll+diff <= uu && lly+diff <= uuy  {
					curr_point := strconv.Itoa(ll+diff) + "," + strconv.Itoa(lly+diff)
					curr_points.Add(curr_point)
					diff += 1
				}
			}
			if !curr_points.Contains(target) {
				curr_points = mapset.NewSet()
			}
			
			diff = 0
			if ll < uu && lly > uuy {
				for ll+diff <= uu && lly-diff >= uuy  {
					curr_point := strconv.Itoa(ll+diff) + "," + strconv.Itoa(lly-diff)
					curr_points.Add(curr_point)
					diff += 1
				}
			}
			if !curr_points.Contains(target) {
				curr_points = mapset.NewSet()
			}

			
			diff = 0
			if ll > uu && lly < uuy {
				for ll-diff >= uu && lly+diff <= uuy  {
					curr_point := strconv.Itoa(ll-diff) + "," + strconv.Itoa(lly+diff)
					curr_points.Add(curr_point)
					diff += 1
				}
			}
			if !curr_points.Contains(target) {
				curr_points = mapset.NewSet()
			}

			diff = 0
			if ll > uu && lly > uuy {
				for ll-diff >= uu && lly-diff >= uuy  {
					curr_point := strconv.Itoa(ll-diff) + "," + strconv.Itoa(lly-diff)
					curr_points.Add(curr_point)
					diff += 1
				}
			}
			if !curr_points.Contains(target) {
				curr_points = mapset.NewSet()
			}
			
			//fmt.Println(l_x, l_y, u_x, u_y, " :====> ", curr_points)
			if curr_points.Cardinality() == 0 {
				fmt.Println(target, "=>", curr_points)
				continue 
			}
			itr := curr_points.Iterator()
			for elem := range itr.C {
				val := elem.(string)
				if _, ok := allPoints2[val]; !ok {
					allPoints2[val] = 0
				}
				allPoints2[val] += 1
				if allPoints2[val] > 1 {
					overLappedPoints2.Add(val)
				}
				//fmt.Println(val)
			}
		}
			/*
			if l_x > u_x {
				ll = u_x
				uu = l_x
				lly = u_y
				uuy = l_y
			} else {
				ll = l_x
				uu = u_x
				lly = l_y
				uuy = u_y
			}
			diff := 0
			var curr_points []string
			for i:=ll;i<uu+1;i++ {
				if lly > uuy {
					diff = -(i-ll)
				} else {
					diff = i-ll
				}
				fmt.Println(ll, ll+i, uu, " ++ ", lly, lly+diff, uuy)
				if ll+i > uu || (lly+diff > uuy && lly < uuy) ||  (lly+diff < uuy && lly > uuy) {
					continue
				}
				curr_point := strconv.Itoa(i) + "," + strconv.Itoa(lly+diff)
				curr_points = append(curr_points, curr_point)
			}
			target := strconv.Itoa(uu) + "," + strconv.Itoa(uuy)
			if len(curr_points) == 0 {
				fmt.Println(target, "=>", curr_points)
				continue 
			}
			if curr_points[len(curr_points)-1] == target {
				for _, val := range curr_points {
					if _, ok := allPoints2[val]; !ok {
						allPoints2[val] = 0
					}
					allPoints2[val] += 1
					if allPoints2[val] > 1 {
						overLappedPoints2.Add(val)
					}
					fmt.Println(val)
				}
			} else {
				// corner case --> just add the points until target (diagnal)
				for _, val := range curr_points {
					if _, ok := allPoints2[val]; !ok {
						allPoints2[val] = 0
					}
					allPoints2[val] += 1
					if allPoints2[val] > 1 {
						overLappedPoints2.Add(val)
					}
					fmt.Println(val)
				}
			}
		}
		fmt.Println(l_x, l_y, u_x, u_y,ll, uu, "--->",allPoints2)
		*/
	}
	//fmt.Println(allPoints2, overLappedPoints2)
	sol2 = overLappedPoints2.Cardinality()

	return sol1, sol2
}