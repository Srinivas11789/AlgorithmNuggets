// Day 8
package main

import (
	//"fmt"
	"strconv"
	"errors"
)

func solve8(input []interface{}) (interface{},interface{}) {

	var day8Inputs [][]int
	visibleMat := [][]int{}

	// Customize input
	for _, val := range input {
		// validate input
		line, ok := val.(string)
		if !ok { panic(errors.New("type cast failed for input")) }
		
		// init
		row := []int{}
		visible_row := []int{}

		// populate the ds
		for i, l := range line {
			// visible trees
			if len(day8Inputs) == 0 || len(day8Inputs) == len(input)-1 {
				visible_row = append(visible_row, 1)
			} else if i == 0 || i == len(line)-1 {
				visible_row = append(visible_row, 1)
			} else {
				visible_row = append(visible_row, 0)
			}
			// add heights
			charac := string(l)
			integer, err := strconv.Atoi(charac)
			if err != nil { panic(err) }
			row = append(row, integer)
		}

		visibleMat = append(visibleMat, visible_row)
		day8Inputs = append(day8Inputs, row)
	}

	// Solution 1
	sol1 := 0

	for i:=0;i<len(day8Inputs);i++ {
		// left to right
		tallTreeFromLeft := 0
		for j:=0;j<len(day8Inputs[0]);j++ {
			treeVisible := false
			if day8Inputs[i][j] > tallTreeFromLeft {
				treeVisible = true
				tallTreeFromLeft = day8Inputs[i][j]
			}
			if visibleMat[i][j] == 1 {
				continue
			}
			if treeVisible {
				visibleMat[i][j] = 1
			}
		}
		// right to left
		tallTreeFromRight := 0
		for j:=len(day8Inputs[0])-1;j>=0;j-- {
			treeVisible := false
			if day8Inputs[i][j] > tallTreeFromRight {
				treeVisible = true
				tallTreeFromRight = day8Inputs[i][j]
			}
			if visibleMat[i][j] == 1 {
				continue
			}
			if treeVisible {
				visibleMat[i][j] = 1
			}
		}
		// top to bottom
		tallTreeFromUp := 0
		for j:=0;j<len(day8Inputs[0]);j++ {
			treeVisible := false
			if day8Inputs[j][i] > tallTreeFromUp {
				treeVisible = true
				tallTreeFromUp = day8Inputs[j][i]
			}
			if visibleMat[j][i] == 1 {
				continue
			}
			if treeVisible {
				visibleMat[j][i] = 1
			}
		}
		// bottom to top
		tallTreeFromDown := 0
		for j:=len(day8Inputs[0])-1;j>=0;j-- {
			treeVisible := false
			if day8Inputs[j][i] > tallTreeFromDown {
				treeVisible = true
				tallTreeFromDown = day8Inputs[j][i]
			}
			if visibleMat[j][i] == 1 {
				continue
			}
			if treeVisible {
				visibleMat[j][i] = 1
			}
		}
	}
	for i:=0;i<len(day8Inputs);i++ {
		for j:=0;j<len(day8Inputs[0]);j++ {
			if visibleMat[i][j] == 1 {
				sol1 += 1
			}
		}
	}

	// Solution 2
	sol2 := 0
	for i:=0;i<len(day8Inputs);i++ {
		for j:=0;j<len(day8Inputs[0]);j++ {
			scenic_score := 1
			for _, k := range [][]int{{-1,0}, {1,0}, {0,-1}, {0,1}} {
				x := i+k[0]
				y := j+k[1]
				view := 0
				for withinRangeMat(x, y, day8Inputs) && day8Inputs[x][y] < day8Inputs[i][j] {						
					view += 1
					x += k[0]
					y += k[1]
				}
				if withinRangeMat(x,y,day8Inputs) && day8Inputs[x][y] >= day8Inputs[i][j] {
					view++
				}
				//fmt.Println("->",x,y,view)
				scenic_score *= view
			}
			//fmt.Println(i,j,scenic_score)
			if scenic_score > sol2 {
				sol2 = scenic_score
			}
		}
	}

	return sol1, sol2
}

func withinRangeMat(x int, y int, matrix [][]int) bool {
	if x < 0 || y < 0 || x >= len(matrix) || y >= len(matrix[0]) {
		return false
	}
	return true
}