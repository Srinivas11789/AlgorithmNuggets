// Day 9
package main

import (
	"fmt"
	"strconv"
	"strings"
)

func printMat(mat [][]string) {
	fmt.Print("\n")
	for _, n := range mat {
		fmt.Println(n)
	}
}

func genRow(num int) []string {
	v := []string{}
	for i:=0;i<num;i++ {
		v = append(v, ".")
	}
	return v
}

func getAdjacentCell(p1, p2 []int) []int {
	/*
	if p1[0] == p2[0] {
		return []int{p1[0], p2[1]-p1[1]}
	} else if p1[1] == p2[1] {
		return []int{p2[0]-p1[0], p1[1]}
	} else {
		return []int{p2[0],p2[0]}
	}
	*/
	return []int{p2[0],p2[0]}
}


func solve9(input []interface{}) (interface{},interface{}) {

	directions := make([]string,0)
	steps := make([]int,0)

	// Customize input
	for _, val := range input {
		nav := strings.Split(val.(string)," ")
		if len(nav) < 2 {
			continue
		}
		step, err := strconv.Atoi(nav[1])
		if err != nil { panic(err) }
		directions = append(directions, nav[0])
		steps = append(steps, step)
	}

	// Solution 1
	sol1 := 0

	// Initial map
	path := [][]string{
		[]string{".", ".", "."},
		[]string{".", ".", "."},
		[]string{".", ".", "."},
	}

	// Directional ref
	dirs := map[string][]int{
		"U": []int{-1, 0},
		"D": []int{1, 0},
		"L": []int{0, -1},
		"R": []int{0, 1},
	}

	// Current pos
	head_x := 2
	head_y := 0
	tail_x := 2
	tail_y := 0
	path[head_x][head_y] = "H"
	path[tail_x][tail_y] = "T"
	prev_x := 2
	prev_y := 0

	// Move head
	for d, dir := range directions {
		step := steps[d]
		for s:=0;s<step;s++ {
			//printMat(path)
			prev_x = head_x
			prev_y = head_y

			// Step
			mx := head_x + dirs[dir][0]
			my := head_y + dirs[dir][1]

			// Path Adjustment
			if mx == len(path) {
				path = append(path, genRow(len(path[0])))
			} else if mx < 0 {
				path = append([][]string{genRow(len(path[0]))}, path...)
				mx = 0
				head_x++
				prev_x++
				tail_x++
			}
			if my == len(path[0]) {
				for i, _ := range path {
					path[i] = append(path[i], ".")
				}
			} else if my < 0 {
				for i, _ := range path {
					path[i] = append([]string{"."}, path[i]...)
				}
				my = 0
				head_y++
				tail_y++
				prev_y++
			}

			// Head and Tail Movement
			if path[head_x][head_y] != "#" && path[head_x][head_y] != "T" {
			    path[head_x][head_y] = "."
			}

			if path[mx][my] != "#" && path[mx][my] != "T" {
				path[mx][my] = "H"
			}
			head_x = mx
			head_y = my

			isAdjacent := false
			// Check for Adjacency
			for _, adj := range [][]int{ {0,1}, {0,-1}, {1,0}, {-1,0}, {1,1}, {-1,-1}, {1,-1}, {-1,1} } {
				adjx := adj[0]+tail_x
				adjy := adj[1]+tail_y
				if adjx == head_x && adjy == head_y  {
					isAdjacent = true
					break
				}
			}
			if isAdjacent {
				continue
			}
			if head_x == tail_x && head_y == tail_y {
				continue
			}

			// Check for straight line movement
			// Check for diagnal movement
			path[tail_x][tail_y] = "#"
			tail_x = prev_x
			tail_y = prev_y
			path[tail_x][tail_y] = "T"
		}
	}

	for _, row := range path {
		for _, c := range row {
			if c == "#" {
				sol1++
			}
			if c == "T" {
				sol1++
			}
		}
	}

	// Solution 2
	sol2 := 0

	// Current pos
	// Initial map
	path = [][]string{
		[]string{".", ".", "."},
		[]string{".", ".", "."},
		[]string{".", ".", "."},
	}

	// 
	head_x = 2
	head_y = 0
	tail_x = 2
	tail_y = 0
	path[head_x][head_y] = "H"
	path[tail_x][tail_y] = "1"
	prev_x = 2
	prev_y = 0
	knots := [][]int{
		{2,0},
		{2,0},
		{2,0},
		{2,0},
		{2,0},
		{2,0},
		{2,0},
		{2,0},
	}

	// Move knotsx
	for d, dir := range directions {
		step := steps[d]
		// Step
		for s:=0;s<step;s++ {
			//printMat(path)

			prev_x = head_x
			prev_y = head_y

			// head move
			mx := head_x + dirs[dir][0]
			my := head_y + dirs[dir][1]

			// Adjust matrix
			if mx == len(path) {
				path = append(path, genRow(len(path[0])))
			} else if mx < 0 {
				path = append([][]string{genRow(len(path[0]))}, path...)
				mx = 0
				head_x++
				tail_x++
				prev_x++
				for i, _ := range knots {
					knots[i][0]++ 
				}
			}
			if my == len(path[0]) {
				for i, _ := range path {
					path[i] = append(path[i], ".")
				}
			} else if my < 0 {
				for i, _ := range path {
					path[i] = append([]string{"."}, path[i]...)
				}
				my = 0
				head_y++
				tail_y++
				prev_y++
				for i, _ := range knots {
					knots[i][1]++ 
				}
			}

			// move position in matrix
			if path[head_x][head_y] == "H" {
				path[head_x][head_y] = "."
			}

			if path[mx][my] == "." {
				path[mx][my] = "H"
			}

			head_x = mx
			head_y = my

			isAdjacent := false
			// Check for Adjacency
			for _, adj := range [][]int{ {0,1}, {0,-1}, {1,0}, {-1,0}, {1,1}, {-1,-1}, {1,-1}, {-1,1} } {
				adjx := adj[0]+tail_x
				adjy := adj[1]+tail_y
				if adjx == head_x && adjy == head_y  {
					isAdjacent = true
					break
				}
			}
			if isAdjacent {
				continue
			}
			if head_x == tail_x && head_y == tail_y {
				continue
			}

			targetPoint := getAdjacentCell([]int{tail_x, tail_y}, []int{prev_x, prev_y})
			front_x := tail_x
			front_y := tail_y

			tail_x = targetPoint[0]
			tail_y = targetPoint[1]
			if path[tail_x][tail_y]  != "#" {
			    path[tail_x][tail_y] = "1"
			}

			// KNots Movement
			for k, _ := range knots {
				kpx := knots[k][0]
				kpy := knots[k][1]
				if k+2 == 9 {
					path[knots[k][0]][knots[k][1]] = "#"
				}

				/*
				for _, dir := range [][]int{{0,1}, {0,-1}, {1,0}, {1,-1}, {1,1}, {-1,-1}, {1, -1}, {-1, 1}} {
					kadjx := knots[k][0] + dir[0]
					kadjy := knots[k][1] + dir[1]
					if kadjx == front_x && kadjy == front_y {
						knots[k][0] = knots[k][0] + dir[0]
						knots[k][1] = knots[k][1] + dir[1]
						break
					}
				}
				*/
				knots[k][0] = front_x
				knots[k][1] = front_y
				front_x = kpx
				front_y = kpy
				if path[knots[k][0]][knots[k][1]] != "#" {
				    path[knots[k][0]][knots[k][1]] = strconv.Itoa(k+2)
				}
			}
		}
	}
	for _, row := range path {
		for _, c := range row {
			if c == "#" {
				sol2++
			}
		}
	}
	
	return sol1, sol2
}