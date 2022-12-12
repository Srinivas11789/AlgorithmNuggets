// Day 2
package main

import (
    //"fmt"
	"strings"
)

func solve2(input []interface{}) (interface{}, interface{}) {

	var day2Inputs [][]string

	// Customize input
	for _, val := range input {
		game, ok := val.(string)
		if !ok { panic("typecast failed") }
		play := strings.Split(game, " ")
		day2Inputs = append(day2Inputs, play)
	}

	abc := map[string]string{
		"A": "Rock",
		"B": "Paper",
		"C": "Scissor",
	}

	score := map[string]int{
		"Rock": 1,
		"Paper": 2,
		"Scissor": 3,
	}

	winner := map[string]string{
		"Rock": "Scissor",
		"Paper": "Rock",
		"Scissor": "Paper",
	}

	loser := map[string]string{
		"Rock": "Paper",
		"Paper": "Scissor",
		"Scissor": "Rock",
	}

	rps := []string{
		"Rock",
		"Paper",
		"Scissor",
	}

	// Solution 1
	sol1 := 0
	max_score := 0
	total_score := 0

	for _,i := range [][]int{{0,1,2}} {
		xyz := map[string]string{
			"X": rps[i[0]],
			"Y": rps[i[1]],
			"Z": rps[i[2]],
		}
		total_score = 0
		for _, game := range day2Inputs {
			p1 := game[0]
			p2 := game[1]
			elf := abc[p1]
			bet := xyz[p2]
			if winner[bet] == elf { // win
				total_score += 6 + score[bet]
			} else if xyz[p2] == elf { // draw
				total_score += 3 + score[bet]
			} else { // loose
				total_score += 0 + score[bet]
			}
			//fmt.Println(total_score, score[bet], bet, elf)
		}
		if total_score > max_score {
			max_score = total_score
		}	
	}
	sol1 = max_score

	// Solution 2
	sol2 := 0
	for _, game := range day2Inputs {
		p1 := game[0]
		p2 := game[1]
		elf := abc[p1]
		if p2 == "X" { // loose
			sol2 += 0 + score[winner[elf]]
		} else if p2 == "Y" { // draw
			sol2 += 3 + score[elf]
		} else { // win
			sol2 += 6 + score[loser[elf]]
		}
		//fmt.Println(elf, p2, loser[elf])
	}
	return sol1, sol2
}