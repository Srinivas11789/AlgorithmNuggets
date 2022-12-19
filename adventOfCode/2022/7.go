// Day 7
package main

import (
	"fmt"
	"strings"
	"errors"
	"strconv"
	"path/filepath"
	"math"
)

type Node struct {
	name string
	typ string
	size   int
	childrens []*Node
}

// Furnish directory size in tree
func dftFillSize(curNode *Node) int {
	dir_sums := 0
	for _, n := range curNode.childrens {
		if n.typ == "file" {
			continue
		}
		dir_sums += dftFillSize(n)
	}
	curNode.size += dir_sums
	return curNode.size
}

// Print nested tree for verification
func printTree(curNode *Node, depth int) {
	meta := fmt.Sprintf("(%s, size=%d)", curNode.typ, curNode.size)
	fmt.Println(strings.Repeat("| ", depth) + "- " + curNode.name + " " + meta)
	for _, c := range curNode.childrens {
		printTree(c, depth+1)
	}
}

func solve7(input []interface{}) (interface{},interface{}) {

	var day7Inputs []string

	// Customize input
	for _, val := range input {
		day7Inputs = append(day7Inputs, val.(string))
	}

	// Solution 1
	sol1 := 0

	// tree construction with root directory
	sol1Tree := Node{
		name: "root",
		size: 0,
		typ: "dir",
		childrens: nil,
	}

	// Init control vars

	// track levels
	levels := map[int][]string{
		0: []string{"root"},
	}
	// memo nodes visited for easy access
	nodes := map[string]*Node{
		"root": &sol1Tree,
	}

	// tree control variables
	curr_level := 1
	curr_parent := &sol1Tree
	curr_dir := "root"

    // Logic

	// iterate until input ceases
	for len(day7Inputs) >= 1 {
		
		// pop the current input
		input := day7Inputs[0]
		if len(day7Inputs) >= 1 {
			day7Inputs = day7Inputs[1:]
		}

		// Proccess only commands (diff from output like ls)
		command := strings.Split(input, " ")
		if command[0] != "$" {
			continue
		}

		// Command processor 
		switch command[1] {
		case "cd": // Directory traversals
			switch command[2] {
		    case "..": // backward directory traversal
				curr_dir = filepath.Join(curr_dir, "../")
				curr_level--
				curr_parent = nil
			case "/": // root primitives (reset)
				curr_parent = nodes["root"]
				curr_dir = "root"
			default: // change directory 
				if curr_level >= len(levels) {
					panic(errors.New("levels out of bounds"))
				}
				for _, n := range levels[curr_level] {
					relative_path := filepath.Join(curr_dir, command[2])
					if n == relative_path {
						curr_parent = nodes[n]
						curr_dir = relative_path
					}
				}
				if curr_parent == nil {
					panic(errors.New("current parent not found: "+command[2]))
				}
				curr_level++
			}
		case "ls": // construct file system
			listOfAssets := [][]string{} // [ [size, file/dir_name] ]
			for len(day7Inputs) >= 1 && !strings.HasPrefix(day7Inputs[0],"$") {
				listOfAssets = append(listOfAssets, strings.Split(day7Inputs[0], " "))
				day7Inputs = day7Inputs[1:]
			}
			for _, asset := range listOfAssets {

				// directory/file primitives
				sizeInt := 0
				currType := "dir"
				if asset[0] != "dir" {
					conv, err := strconv.Atoi(asset[0])
					if err != nil { panic(err) }
					sizeInt = conv
					currType = "file"
				}

				// current node primitives (create a file/dir)
				relative_name := curr_parent.name + "/" + asset[1]
				currNode := Node{
					name: relative_name,
					typ: currType,
					size: sizeInt,
					childrens: nil,
				}

				// tree hierarchy arrangement and memo
				curr_parent.childrens = append(curr_parent.childrens, &currNode)
				curr_parent.size += sizeInt
				nodes[relative_name] = &currNode
				if _, ok := levels[curr_level]; !ok {
					levels[curr_level] = []string{}
				}
				levels[curr_level] = append(levels[curr_level], relative_name)
			}
		}
	}

	// calculate size by traversing the tree from root
	dftFillSize(nodes["root"])
	//printTree(nodes["root"], 0)
	
	// sol1
	for _, c := range nodes {
		if c.typ == "dir" && c.size <= 100000 {
			sol1 += c.size
		}
	}

	// Solution 2
	sol2 := 0
	total_fs := 70000000
	req_space := 30000000
	current_free_space := total_fs - nodes["root"].size
	current_req_space := req_space - current_free_space
	delta := math.MaxInt
	var selected *Node
	for _, n := range nodes {
		if n.typ == "file" { continue }
		curr_delta := n.size-current_req_space
		if curr_delta >= 0 && curr_delta < delta {
			delta = curr_delta
			selected = n
		}
	}
	sol2 = selected.size

	return sol1, sol2
}