// 101 Recursive
package main
import "fmt"

func factorial(n int) int {
    if n == 0 {
        return 0;
    } else if n == 1 {
        return 1;
    } else {
        return factorial(n-1)*n;
    }
}

func main() {
    //Enter your code here. Read input from STDIN. Print output to STDOUT
    var n int;
    fmt.Scanf("%d",&n);
    fmt.Print(factorial(n));
}
