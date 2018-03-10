//Array

package main
import "fmt"

func main() {
    //Enter your code here. Read input from STDIN. Print output to STDOUT
    var n int;
    fmt.Scanf("%d",&n);
    arr := make([]int,n);
    for i:=0;i<n;i++ {
        fmt.Scanf("%d",&arr[i]);
    }
    //fmt.Println(arr);
    for i:=n-1;i>=0;i-- {
        fmt.Print(arr[i]," ");
    }
}
