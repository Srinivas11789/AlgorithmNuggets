package main

import ( 
          "fmt" 
)

func main() {
   
   fmt.Println("This Program is used to list the Fibonacci Series !")
   var n int
   fmt.Print("Enter the number of Fibo to Print : ")
   fmt.Scanf("%d",&n)
   fmt.Println("The Number Selected is :",n)
   var first int = 0
   var second int = 1
   var i int
   var next int
   for i=0; i < n; i++ {
      next = first + second
      fmt.Print(next, " ")
      first = second
      second = next
   }
   fmt.Println("")
   fmt.Println("End")
}
