package main

import (
         "fmt"
       )

func fibo(i int) (int) {
   if i == 0 {
     return 0
   }
   if i == 1 {
     return 1
   } else {
     return  fibo(i-1) + fibo(i-2)
  }
}


func main() {
   fmt.Println("Fibonacci Series - Recursion")
   var n int
   fmt.Print("Enter the Number of Fibo Number you want to print: ")
   fmt.Scanf("%d",&n)
   var i int
   for i=0; i<n; i++ {  
      fmt.Print(fibo(i), " ")
   }
   fmt.Println("")
   fmt.Println("END")
}

