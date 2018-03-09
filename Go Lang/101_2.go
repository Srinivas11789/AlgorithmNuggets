# Data Types

package main


import (
  "fmt"
  "os"
  "bufio"
  "strconv"
)

func main() {
  	var _ = strconv.Itoa // Ignore this comment. You can still use the package "strconv".
  
    var i uint64 = 4
    var d float64 = 4.0
    var s string = "HackerRank "

    scanner := bufio.NewScanner(os.Stdin)

# User Code

    
    // Declare second integer, double, and String variables.
    //var i1 uint64;
    //var d1 float64;
    //var s1 string;
    var inputs [3]string;
    var j int = 0;

    // Read and save an integer, double, and String to your variables.
    for (scanner.Scan()){
        inputs[j] = scanner.Text()
        j = j+1
    }
    //i1, _ := strconv.Atoi(inputs[0]);
    i1, _ := strconv.ParseUint(inputs[0],10,64);
    d1, _ := strconv.ParseFloat(inputs[1],64);
    s1 := inputs[2];
    //sum := strconv.FormatFloat(d+d1, 'E', -1, 64)


    
    // Print the sum of both integer variables on a new line.
    //fmt.Println(inputs);
    //fmt.Println(i1+i,i,d,s);
    fmt.Println(i1+i);
    fmt.Printf("%0.1f\n",d+d1);
    fmt.Println(s+s1);

    // Print the sum of the double variables on a new line.
    //fmt.Println(d);

    // Concatenate and print the String variables on a new line
    // The 's' variable above should be printed first.
    //fmt.Println(s+s1);


