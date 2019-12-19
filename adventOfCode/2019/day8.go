/*
--- Day 8: Space Image Format ---
The Elves' spirits are lifted when they realize you have an opportunity to reboot one of their Mars rovers, and so they are curious if you would spend a brief sojourn on Mars. You land your ship near the rover.

When you reach the rover, you discover that it's already in the process of rebooting! It's just waiting for someone to enter a BIOS password. The Elf responsible for the rover takes a picture of the password (your puzzle input) and sends it to you via the Digital Sending Network.

Unfortunately, images sent via the Digital Sending Network aren't encoded with any normal encoding; instead, they're encoded in a special Space Image Format. None of the Elves seem to remember why this is the case. They send you the instructions to decode it.

Images are sent as a series of digits that each represent the color of a single pixel. The digits fill each row of the image left-to-right, then move downward to the next row, filling rows top-to-bottom until every pixel of the image is filled.

Each image actually consists of a series of identically-sized layers that are filled in this way. So, the first digit corresponds to the top-left pixel of the first layer, the second digit corresponds to the pixel to the right of that on the same layer, and so on until the last digit, which corresponds to the bottom-right pixel of the last layer.

For example, given an image 3 pixels wide and 2 pixels tall, the image data 123456789012 corresponds to the following image layers:

Layer 1: 123
         456

Layer 2: 789
         012
The image you received is 25 pixels wide and 6 pixels tall.

To make sure the image wasn't corrupted during transmission, the Elves would like you to find the layer that contains the fewest 0 digits. On that layer, what is the number of 1 digits multiplied by the number of 2 digits?
*/

package main

import (
    "fmt"
    "os"
    "bufio"
    "strings"
)

func part1_assigned_user_input(n string) (int) {

    // Open the file.
    f, _ := os.Open("day"+n+".input")
   
    // Create a Scanner for the file
    scanner := bufio.NewScanner(f)

    var encoded_data []string;
  
    // Create a GRAPH with hashmap or dict for the inputs
    for scanner.Scan() {
        encoded_data = strings.Split(scanner.Text(), "");
        //fmt.Println(encoded_data);
    }

    // Decode image data
    return decode_image(encoded_data, 1);
  }

func decode_image(encoded_data []string, part int) (int) {
    // As per input we need to create the layer 25 wide x 6 tall

    // Part 1 Params
    count0 := int(^uint(0) >> 1);
    count1 := 0;
    count2 := 0;
    var min_zero_layer []string;

    var decode_data [][]string;
    i := 0;
    for i < len(encoded_data) {
        var current_layer []string;
        var current_zero int;
        tall := 0;
        for tall < 6 {
            width := 0;
            for width < 25 {
                if encoded_data[i] == "0" {
                    current_zero += 1;
                }
                current_layer = append(current_layer, encoded_data[i]);
                i += 1;
                width += 1;
            }
            //i += 1;
            tall += 1;
        }
        if current_zero < count0 {
            count0 = current_zero;
            min_zero_layer = current_layer;
        }
        decode_data = append(decode_data, current_layer);
    }
    //fmt.Println(decode_data);
    //fmt.Println(min_zero_layer);
    for i:=0; i<len(min_zero_layer); i++ {
        if min_zero_layer[i] == "1" {
            count1 += 1;
        }
        if min_zero_layer[i] == "2" {
            count2 += 1;
        }
    }
    return count1*count2;
}

func main() {
    day := "8";
    fmt.Println("Day "+ day +" of Advent-Of-Code!...");
    
    // Program assigned user input
    result1 := part1_assigned_user_input(day);
  
    fmt.Println("Solution to Day "+ day +" is: ");
    fmt.Println("* Part 1: program assigned-user input solution is: ", result1);
  }