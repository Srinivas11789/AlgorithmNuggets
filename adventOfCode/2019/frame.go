/*
Day N Question
*/

package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
  //"math"
  "os"
  "bufio"
  //"strconv"
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

func part1_assigned_user_input(n string) (int) {
  //input, err := ioutil.ReadFile("day"+n+".input")
  
  // Open the file.
  f, _ := os.Open("day"+n+".input")
 
  // Create a Scanner for the file
  scanner := bufio.NewScanner(f)

  // Read and print each line in the file
  var result int;
  for scanner.Scan() {
    // solve 
  }
 
  return result 
}

func part2_assigned_user_input(n string) (int) {
  // Open the file.
  f, _ := os.Open("day"+n+".input")

  // Create a Scanner for the file
  scanner := bufio.NewScanner(f)

  // Read and print each line in the file
  var result int;
  for scanner.Scan() {
    // solve
  }
  return result;
}

func solve_problem(num int) int {
  // core formula to solve
  return 0;
}

func main() {
  day := "N";
  fmt.Println("Day "+ day +" of Advent-Of-Code!...");
  
  // Program non-user input
  input, err := get_input(day);
  if err != nil {
    fmt.Println("Cannot get the non-user first input for the problem!");
  }

  var result int;
  for _, value := range input {
    result += solve_problem(int(value));
  }
  
  // Program assigned user input
  result2 := part1_assigned_user_input(day);

  fmt.Println("Solution to Day "+ day +" is: ");
  fmt.Println("* Part 1: program non-user input solution is: ", result);
  fmt.Println("* Part 1: program assigned-user input solution is: ", result2);
  //fmt.Println(input);
  fmt.Println("* Part 2: program assigned-user input solution is: ", part2_assigned_user_input(day));
  
}
