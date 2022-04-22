package main
// Iterate the day problems --> read inputs --> execute the solution --> print result

import (
	ioutil "io/ioutil"
	"strconv"
	"strings"
	"fmt"
)

func main() {
	dayChallenges := map[int]func(input []interface{})(int,int) {
		1: solve1,
		2: solve2,
		3: solve3,
		4: solve4,
		5: solve5,
		6: solve6,
		7: solve7,
		8: solve8,
	}
	// Iterate day inputs
	for day, fun := range dayChallenges {
		folderName := strconv.Itoa(day)
		inputFiles := []string{folderName+"-sample" + ".input", folderName + ".input"}
		for _, f := range inputFiles {
			var inputs []interface{}
			body, err := ioutil.ReadFile(folderName + "/" + f)
			if err != nil { panic(err) }
			input_strs := strings.Split(string(body), "\n")
			for _, val := range input_strs {
				if val == "" { continue }
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