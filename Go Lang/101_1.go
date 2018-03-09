package main

import (
    "fmt"
    "bufio"
    "os"
)

func main() {
    //fmt.Scan(&ip); For userinput to be an INT else STRING until a space
    reader := bufio.NewReader(os.Stdin);
    ip, _ := reader.ReadString('\n'); //watch out for single quotes here, double quotes might lead to error in consideration of a string
    fmt.Println("Hello, World.");
    fmt.Println(ip);
}
