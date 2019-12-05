/*

Day 4 Question - Reference to https://adventofcode.com/2019/day/4

--- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle answer was 979.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?

Your puzzle input is still 256310-732736.
*/

package main

import (
  "fmt"
  "strconv"
)

// Part 1 Solution
func part1_assigned_user_input(n string) (int) {  

	// Count of possible passwords
	count := 0;

	// Loop through the answer range ( might differ depend on the user )
	for i := 256310; i <= 732736; i++ {

	  // convert the num to string to operate and compare
	  num := string(strconv.Itoa(i));

	  // Adjacent same critera detection
	  alternate := false;

	  // Current index location
	  current := 0;
	  
	  // Last value visited
	  parent := int(num[0]);
	 
	  // Iterate through the number string
      for index, value := range num {
		  // Alter the current index
		  current = index;
		  // Rule 1 fails --> digits should keep increasing
		  if index > 0 && parent > int(value) {
			index = 0;
			alternate = false;
            break;
		  }
		  // Rule 2 success --> Same alternate 
		  if index > 0 && int(value) == int(parent) {
			alternate = true;
		  } else {
			parent = int(value);
		  }
	  }
	  if ( alternate == true && current == len(num)-1 ) {
		//fmt.Println(num, alternate, current);
		count += 1;
	  }
	}
	return count;
}

func part2_assigned_user_input(n string) (int) {  
	count := 0;
	//for i := 123455; i <= 123455; i++ {
	for i := 256310; i <= 732736; i++ {
	  num := string(strconv.Itoa(i));
	  alternate := false;
	  current := 0;
	  parent := int(num[0]);
	  times := 0;
	  //freq := map[string]int{};
      for index, value := range num {
		  current = index;
		  if index > 0 && parent > int(value) { // Rule 1 Fail --> if decreases 
			index = 0;
			alternate = false;
            break;
		  } else if index > 0 && int(value) == parent { // Rule 2 success --> Same alternate
			times += 1;
			//freq[parent] = times;
			if times == 2 && current == len(num)-1 {
				alternate = true;
			}
		  } else { // Rule 3 success --> Same alternate not in a bigger group
			  if times >= 2 && alternate == false {
				//fmt.Println("change", times, num, index, int(value), times);
				if times == 2 {
				  alternate = true;
				}
			   }
			   // Reset match counter
			  times = 1;
		  }
		  // track a parent or previous value for matching
		  parent = int(value);
		}
		// Update counter when all the rules match 
		if ( alternate == true && current == len(num)-1 ) {
			//fmt.Println("----->", num, alternate, current);
			count += 1;
		}
    }
	return count;
}


func main() {
  day := "4";
  fmt.Println("Day "+ day +" of Advent-Of-Code!...");
  result := part1_assigned_user_input(day);
  result2 := part2_assigned_user_input(day);
  fmt.Println("Solution to Day "+ day +" is: ");
  fmt.Println("* Part 1: program assigned-user input solution is: ", result);
  fmt.Println("* Part 2: program assigned-user input solution is: ", result2);
}