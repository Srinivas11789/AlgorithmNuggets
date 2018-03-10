// 2D Array with max hourglass count

package main
import "fmt"

func main() {
    //Enter your code here. Read input from STDIN. Print output to STDOUT
    n := 6;
    //count := 0;
    var max int;
    max = -65535;
    var sum int;
    sum =0;
    arr := make([][]int,n);
    for i := range arr {
        arr[i] = make([]int, n);
    }
    for i:=0;i<n;i++ {
        for j:=0;j<n;j++ {
            fmt.Scanf("%d",&arr[i][j]);
        }
    }
    for i:=0;i<n;i++ {
        for j:=0;j<n;j++ {
            sum = 0;
            if (i > 0 && i < n-1) && (j > 0 && j < n-1) {
                //fmt.Println(i,j);
                //fmt.Println(-1+5);
                sum = arr[i][j]+arr[i-1][j-1]+arr[i-1][j+1]+arr[i+1][j-1]+arr[i+1][j+1]+arr[i-1][j]+arr[i+1][j];
                //fmt.Println(sum);
            if sum > max {
                    //fmt.Println(sum);
                    max = sum;
                    //fmt.Println(max);
                } 
        }
    }
    }
    fmt.Print(max);
}
