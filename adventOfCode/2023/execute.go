package main

// Iterate the day problems --> read inputs --> execute the solution --> print result

import (
	"fmt"
	ioutil "io/ioutil"
	"strconv"
	"strings"
)

func main() {
	dayChallenges := map[int]func(input []interface{}) (interface{}, interface{}){
		1: solve1,
	}
	// Iterate day inputs
	for day, fun := range dayChallenges {
		folderName := strconv.Itoa(day)
		inputFiles := []string{folderName + "-sample" + ".input", folderName + ".input"}
		for _, f := range inputFiles {
			var inputs []interface{}
			body, err := ioutil.ReadFile(folderName + "/" + f)
			if err != nil {
				panic(err)
			}
			input_strs := strings.Split(string(body), "\n")
			for _, val := range input_strs {
				inputs = append(inputs, val)
			}
			if strings.Contains(f, "sample") {
				fmt.Print("[Samples] Day " + folderName + ":")
			} else {
				fmt.Print("[Problem] Day " + folderName + ":")
			}
			fmt.Println(fun(inputs))
		}
	}
}
