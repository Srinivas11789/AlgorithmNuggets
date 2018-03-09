package main
import "fmt"

func main() {
    //Enter your code here. Read input from STDIN. Print output to STDOUT
    var n int;
    var k int;
    fmt.Scanf("%d %d",&n,&k);
    elements := make([]int,n);
    for i:=0;i<n;i++ {
        fmt.Scanf("%d",&elements[i]);
    }
    //fmt.Println(elements);
    answer := make([]int,n);
    for i:=0;i<n;i++ {
        j := i - k;
        if j < 0 {
            j = n+j
        }
        answer[j] = elements[i]
    }
    for i:=0;i<n;i++ {
        fmt.Print(answer[i]," ");
    }
}
