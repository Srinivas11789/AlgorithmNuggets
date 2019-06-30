package kata

import (
     "math"
)

// O(N2) Iteration ends in timeout alter logic
func RemovNb1(m uint64) [][2]uint64 {
     var result [][2]uint64
     var i,j uint64
     total := sumi(m)
     //fmt.Println(total)
     for i = 0; i < m; i++ {
         for j = i+1; j < m; j++ {
             if total-i-j == i*j {
                //fmt.Println(i,j)
                result = append(result, [2]uint64{i, j}, [2]uint64{j, i})
             }
         }
     }
     return result
}

func RemovNb(m uint64) [][2]uint64 {
     var result [][2]uint64
     var i uint64
     var temp float64
     total := sumi(m)
     //fmt.Println(total)
     for i = 1; i < m; i++ {
          //temp = (total-i)%i
          //if temp*i == total-i-temp {
          //    result = append(result, [2]uint64{i, temp})
          //}
          temp = (float64(total)-float64(i))/(float64(i)+1)
          if temp < float64(m) && math.Trunc(temp) == temp {
            result = append(result, [2]uint64{i, uint64(temp)})
          }
     }
     if len(result) > 0 {
       return result
     } else {
       return nil
     }
}

// Sum of the n numbers
func sumi(value uint64) uint64 {
    var result uint64
    var i uint64
    result = 0
    for i=0; i <= value; i++ {
        result += i
    }
    return result
}
