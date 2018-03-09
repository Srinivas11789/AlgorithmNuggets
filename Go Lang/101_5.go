// Loops

package main
import "fmt"

func main() {
    //Enter your code here. Read input from STDIN. Print output to STDOUT
    var input int;
    fmt.Scanf("%d",&input);
    for i:=1;i<11;i++ {
        fmt.Println(input,"x",i,"=",input*i);
    }
}
