/*
--- Day 1: The Tyranny of the Rocket Equation ---
Santa has become stranded at the edge of the Solar System while delivering presents to other planets! To accurately calculate his position in space, safely align his warp drive, and return to Earth in time to save Christmas, he needs you to bring him measurements from fifty stars.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

The Elves quickly load you into a spacecraft and prepare to launch.

At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't determined the amount of fuel required yet.

Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?
*/

package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
  "math"
  "os"
  "bufio"
  "strconv"
)

func get_input() ([]byte, error) {
  resp, err := http.Get("https://adventofcode.com/2019/day/1/input");
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
  //fmt.Println(body);
  return body, nil;
}

func part1_assigned_user_input() (int) {
  //input, err := ioutil.ReadFile("day1.input")
  
  // Open the file.
  f, _ := os.Open("day1.input")
 
  // Create a Scanner for the file
  scanner := bufio.NewScanner(f)

  // Read and print each line in the file
  var result int;
  for scanner.Scan() {
    num, _ := strconv.Atoi(scanner.Text())
    result += solve_problem(num);
  }
 
  return result 
}

func part2_assigned_user_input() (int) {
  // Open the file.
  f, _ := os.Open("day1.input")

  // Create a Scanner for the file
  scanner := bufio.NewScanner(f)

  // Read and print each line in the file
  var result int;
  for scanner.Scan() {
    num, _ := strconv.Atoi(scanner.Text());
    next := solve_problem(num);
    current := next;
    for ( next >= 0 ) {
      //fmt.Println(next, current);
      next = solve_problem(next);
      if ( next > 0 ) {
        current += next;
      }
    }
    //fmt.Println(num, current);
    result += current;
  }
  return result;
}

func solve_problem(num int) int {
  return int(math.Round(float64(num/3.0))-2)
}

func main() {
  fmt.Println("Day 1 of Advent-Of-Code!...");
  
  // Program non-user input
  input, err := get_input();
  if err != nil {
    fmt.Println("Cannot get the non-user first input for the problem!");
  }

  var result int;
  for _, value := range input {
    result += solve_problem(int(value));
  }
  
  // Program assigned user input
  result2 := part1_assigned_user_input();

  fmt.Println("Solution to Day 1 is: ");
  fmt.Println("* Part 1: program non-user input solution is: ", result);
  fmt.Println("* Part 1: program assigned-user input solution is: ", result2);
  //fmt.Println(input);
  fmt.Println("* Part 2: program assigned-user input solution is: ", part2_assigned_user_input());
  
}
