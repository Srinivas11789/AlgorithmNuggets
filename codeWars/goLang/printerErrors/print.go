package kata

import (
    //"fmt"
    "strconv"
    )

func PrinterError(s string) string {
     denominator := len(s)
     numerator := 0
     //fmt.Println(s)
     for i := 0; i < denominator; i ++ {
         //fmt.Println(s[i]) // prints in octal value
         if s[i] < 97 || s[i] > 109 {
             numerator ++
         }
         //fmt.Println(numerator)
     }
     return strconv.Itoa(numerator)+"/"+strconv.Itoa(denominator)
}
