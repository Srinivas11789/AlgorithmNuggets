// Day 4
package main

import (
	//"fmt"
	"strings"
	"strconv"
)

func returnProcessedInputs(input []interface{}) ([]int, [][][]int) {
	var day4NumbersDraw []int
	var dar4Cards [][][]int

	// Customize input
    day4NumbersDrawString := strings.Split(input[0].(string), ",")
	for _, val := range day4NumbersDrawString {
		stripedInt := strings.TrimSpace(val)
		inte, err := strconv.Atoi(stripedInt)
		if err != nil {
			panic(err)
		}
		day4NumbersDraw = append(day4NumbersDraw, inte)
	}

	current_card := [][]int{}
	for index, val := range input {
		if index == 0 { continue }
		if (index-1)%5 == 0  {
			if len(current_card) > 0 {
				dar4Cards = append(dar4Cards, current_card)
			}
			current_card = [][]int{}
		}
		curr_row := []int{}
		elements := strings.Split(val.(string), " ")
		for _, e := range elements {
			stripedInt := strings.TrimSpace(e)
			if stripedInt == "" {
				continue
			}
			inte, err := strconv.Atoi(stripedInt)
			if err != nil {
				panic(err)
			}
			curr_row = append(curr_row, inte)
		}
		current_card = append(current_card, curr_row)
	}
	dar4Cards = append(dar4Cards, current_card)

	return day4NumbersDraw, dar4Cards
}

func verifyWinner(card [][]int) bool {
	for i, _ := range card {
		rowWin := 0
		colWin := 0
		for j, _ := range card[i] {
			if card[i][j] == -1 {
				rowWin += 1
			}
			if card[j][i] == -1 {
				colWin += 1
			}
		}
		//fmt.Print(rowWin, colWin, len(card[i]))
		if rowWin == len(card[i]) || colWin == len(card[i]) {
			return true
		}
	}
	return false
}

func markCard(card [][]int, draw int) [][]int {
	//fmt.Println("before marking: ", draw, card)
	for i, _  := range card {
		for j, _  := range card[i] {
			if card[i][j] == draw {
				card[i][j] = -1
			}
			if card[j][i] == draw {
				card[j][i] = -1
			}
 		}
	}
	//fmt.Println("after marking: ", draw, card)
	return card
}

func addAllNonVisited(card [][]int) int {
	total := 0
	for i, _  := range card {
		for j, _  := range card[i] {
			if card[i][j] != -1 {
				total += card[i][j]
			}
 		}
	}
	return total
}

func solve4(input []interface{}) (int, int) {

	day4NumbersDraw, dar4Cards := returnProcessedInputs(input)

	// Solution 1
	sol1 := 0
	winnerDraw := -1
	winnerCardNo := -1
	for _, draw := range day4NumbersDraw {
		for i, _ := range dar4Cards {
			dar4Cards[i] = markCard(dar4Cards[i], draw)
			if verifyWinner(dar4Cards[i]) {
				winnerDraw = draw
				winnerCardNo = i
				break
			}
		}
		if winnerDraw != -1 {
			break
		}
	}
	//fmt.Println("winner:", dar4Cards, winnerDraw)
	sol1 = addAllNonVisited(dar4Cards[winnerCardNo]) * winnerDraw

	// Solution 2
	sol2 := 0
	winnerCardsDraw := make(map[int]int)
	winnerCard := -1
	for _, draw := range day4NumbersDraw {
		for i, _ := range dar4Cards {
			dar4Cards[i] = markCard(dar4Cards[i], draw)
			if verifyWinner(dar4Cards[i]) {
				if _, ok := winnerCardsDraw[i]; !ok {
					if len(winnerCardsDraw) == len(dar4Cards)-1 {
						winnerCard = i
					}
					winnerCardsDraw[i] = draw
				}
			}
		}
		if winnerCard != -1 {
			break
		}
	}
	sol2 = addAllNonVisited(dar4Cards[winnerCard]) * winnerCardsDraw[winnerCard]

	return sol1, sol2
}