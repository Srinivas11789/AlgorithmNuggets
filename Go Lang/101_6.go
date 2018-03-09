// Review Challenge
package main
import (
    "fmt"
    "strings"
)

func main() {
    //Enter your code here. Read input from STDIN. Print output to STDOUT
    var n int;
    fmt.Scanf("%d",&n);
    s :=make([]string, n);
    for i:=0;i<n;i++ {
        fmt.Scan(&s[i]);
        current := strings.Split(s[i], "");
        evenStr := "";
        oddStr := "";
        for j:=0;j<len(s[i]);j++ {
            if j%2 == 0 {
                evenStr += current[j];
            } else {
                oddStr += current[j];
            }
        }
        fmt.Println(evenStr,oddStr);
    }
}
