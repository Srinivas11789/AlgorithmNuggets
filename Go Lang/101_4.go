// 101 Conditional Flow
package main
import "fmt"

func main() {
 //Enter your code here. Read input from STDIN. Print output to STDOUT
    var input int;
    fmt.Scanf("%d",&input);
    //fmt.Println(input);
    if input % 2 == 0 {
        if input >= 2 && input <=5 {
            fmt.Println("Not Weird");
        } else if input > 5 && input < 21 {
            fmt.Println("Weird");
        } else {
            fmt.Println("Not Weird");
        }
    } else {
        fmt.Println("Weird");
    }
}
