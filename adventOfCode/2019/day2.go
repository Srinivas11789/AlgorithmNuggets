/*
Day 2 Question - Reference to https://adventofcode.com/2019/day/2

--- Day 2: 1202 Program Alarm ---
On the way to your gravity assist around the Moon, your ship computer beeps angrily about a "1202 program alarm". On the radio, an Elf is already explaining how to handle the situation: "Don't worry, that's perfectly norma--" The ship computer bursts into flames.

You notify the Elves that the computer's magic smoke seems to have escaped. "That computer ran Intcode programs like the gravity assist program it was working on; surely there are enough spare parts up there to build a new Intcode computer!"

An Intcode program is a list of integers separated by commas (like 1,0,0,3,99). To run one, start by looking at the first integer (called position 0). Here, you will find an opcode - either 1, 2, or 99. The opcode indicates what to do; for example, 99 means that the program is finished and should immediately halt. Encountering an unknown opcode means something went wrong.

Opcode 1 adds together numbers read from two positions and stores the result in a third position. The three integers immediately after the opcode tell you these three positions - the first two indicate the positions from which you should read the input values, and the third indicates the position at which the output should be stored.

For example, if your Intcode computer encounters 1,10,20,30, it should read the values at positions 10 and 20, add those values, and then overwrite the value at position 30 with their sum.

Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.

Once you're done processing an opcode, move to the next one by stepping forward 4 positions.

For example, suppose you have the following program:

1,9,10,3,2,3,11,0,99,30,40,50
For the purposes of illustration, here is the same program split into multiple lines:

1,9,10,3,
2,3,11,0,
99,
30,40,50
The first four integers, 1,9,10,3, are at positions 0, 1, 2, and 3. Together, they represent the first opcode (1, addition), the positions of the two inputs (9 and 10), and the position of the output (3). To handle this opcode, you first need to get the values at the input positions: position 9 contains 30, and position 10 contains 40. Add these numbers together to get 70. Then, store this value at the output position; here, the output position (3) is at position 3, so it overwrites itself. Afterward, the program looks like this:

1,9,10,70,
2,3,11,0,
99,
30,40,50
Step forward 4 positions to reach the next opcode, 2. This opcode works just like the previous, but it multiplies instead of adding. The inputs are at positions 3 and 11; these positions contain 70 and 50 respectively. Multiplying these produces 3500; this is stored at position 0:

3500,9,10,70,
2,3,11,0,
99,
30,40,50
Stepping forward 4 more positions arrives at opcode 99, halting the program.

Here are the initial and final states of a few more small programs:

1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.
Once you have a working computer, the first step is to restore the gravity assist program (your puzzle input) to the "1202 program alarm" state it had just before the last computer caught fire. To do this, before running the program, replace position 1 with the value 12 and replace position 2 with the value 2. What value is left at position 0 after the program halts?
*/

package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
  //"math"
  "os"
  "bufio"
  "strconv"
  "strings"
)

// Get the input for the program as anonymous user

func get_input(n string) ([]byte, error) {
  resp, err := http.Get("https://adventofcode.com/2019/day/" + n+ "/input");
  if err != nil {
    fmt.Println("Cannot get the input for the problem!");
    return []byte{}, err;
  }
  body, err := ioutil.ReadAll(resp.Body);
  if err != nil {
    fmt.Println("Cannot get the input for the problem!");
    return []byte{}, err;
  }
  defer resp.Body.Close();
  return body, nil;
}

func part1_assigned_user_input(n string) ([]int) {
  //input, err := ioutil.ReadFile("day"+n+".input")
  
  // Open the file.
  f, _ := os.Open("day"+n+".input")
 
  // Create a Scanner for the file
  scanner := bufio.NewScanner(f)
  var lines []int;

  for scanner.Scan() {
      line := strings.Split(scanner.Text(), ",");
      for _, value := range line {
        num, _ := strconv.Atoi(value);
        lines = append(lines, num);
      }
  }

  // Read and print each line in the file
  return solve_problem(lines, "1");
}

func part2_assigned_user_input(n string) ([]int) {
  //input, err := ioutil.ReadFile("day"+n+".input")
  
  // Open the file.
  f, _ := os.Open("day"+n+".input")
 
  // Create a Scanner for the file
  scanner := bufio.NewScanner(f)
  var lines []int;

  for scanner.Scan() {
      line := strings.Split(scanner.Text(), ",");
      for _, value := range line {
        num, _ := strconv.Atoi(value);
        lines = append(lines, num);
      }
  }

  // Read and print each line in the file
  return solve_problem(lines, "2");
}

func solve_problem(input []int, part string) []int {
  // core formula to solve
  
  // 1. Get opcode (decide operation) and jump the indexes (3) - 2 operands and 1 result
  i := 0;
  end_program := 99;
  var opcode int;
  var op1 int;
  var op2 int;
  var target int;
  var result int;

  if ( part == "1" ) {
    // 2. Initialize program to 1202 state
    input[1] = 12;
    input[2] = 2;

    //fmt.Println(input);

    // 3. Iterate == run program
    for ( input[i] != end_program ) {
      opcode = input[i];
      op1 = input[i+1];
      op2 = input[i+2];
      target = input[i+3];
      if ( opcode == 1 ) {
        result = input[op1] + input[op2];
      } else {
        result = input[op1]*input[op2];
      }
      //fmt.Println(input, opcode, op1, op2, target, result);
      input[target] = result;
      i += 4;
    }

    // 4. Return the zeroth index
    return []int{input[0]};
  } else {
    // 2. Initialize program to 1202 state
    for k := 1; k < 100; k++ {
      for j := 1; j < 100; j++ {
        // 2. Initialize program to 1202 state
        //new_input := input;
        new_input := make([]int, len(input)); 
        copy(new_input, input); 
        //fmt.Println(k,j,new_input, input);
        i := 0;
        new_input[1] = k;
        new_input[2] = j;
        // 3. Iterate == run program
        for ( new_input[i] != end_program ) {
          opcode = new_input[i];
          op1 = new_input[i+1];
          op2 = new_input[i+2];
          target = new_input[i+3];
          if ( opcode == 1 ) {
            result = new_input[op1] + new_input[op2];
          } else {
            result = new_input[op1] * new_input[op2];
          }
          //fmt.Println(input, opcode, op1, op2, target, result);
          new_input[target] = result;
          i += 4;
        }
        if new_input[0] == 19690720 {
          return []int{100*k+j}
        }
      }
    }   

    // 4. Return the zeroth index
    return []int{input[0]};
  }
}

func main() {
  day := "2";
  fmt.Println("Day "+ day +" of Advent-Of-Code!...");
  
  // Program non-user input
  input, err := get_input(day);
  if err != nil {
    fmt.Println("Cannot get the non-user first input for the problem!");
  }
 
  var input_arr []int;
  for _, value := range input {
    input_arr = append(input_arr, int(value));
  }

  // anonymous input solve
  //result := solve_problem(input_arr);
  
  // Program assigned user input - part 1
  result2 := part1_assigned_user_input(day);
  result3 := part2_assigned_user_input(day);

  fmt.Println("Solution to Day "+ day +" is: ");
  //fmt.Println("* Part 1: program non-user input solution is: ", result);
  fmt.Println("* Part 1: program assigned-user input solution is: ", result2);
  //fmt.Println(input);
  fmt.Println("* Part 2: program assigned-user input solution is: ", result3);
}
