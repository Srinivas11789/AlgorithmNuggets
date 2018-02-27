package main

import (
         "fmt"
       )

func memo_fibo(i int) (int) {
   var memo [1000]int
   var minus1 int
   var minus2 int
   if i == 0 {
      return 0
   } else if i == 1 {
      return 1
   } else { 
     if memo[i-1] > 0 {
        minus1 = memo[i-1]
        fmt.Println("Memoized for entry",i,"is",minus1)
     } else {
        minus1 = memo_fibo(i-1)
     }
     if memo[i-2] > 0 {
        minus2 = memo[i-2]
        fmt.Println("Memoized for entry",i,"is",minus2)
     } else {
        minus2 = memo_fibo(i-2)
     }
     return minus1 + minus2
   }
}


func main() {
   fmt.Println("Fibonacci Series - Recursion")
   var n int
   fmt.Print("Enter the Number of Fibo Number you want to print: ")
   fmt.Scanf("%d",&n)
   var i int
   for i=0; i<n; i++ {  
      fmt.Print(memo_fibo(i), " ")
   }
   fmt.Println("")
   fmt.Println("END")
}

