# Logic 1: Split and check each octets
package kata

import (
    "strings"
    "strconv"
)

func Is_valid_ip(ip string) bool {
  octets := strings.Split(ip, ".")
  if len(octets) == 4 {
     for i := 0; i<4; i++ {
         octet, err := strconv.Atoi(octets[i])
         ztest := strconv.Itoa(octet)
         if err != nil {
            return false
         }
         if octets[i] != ztest {
             return false
         }
         if octet < 0 || octet > 255 {
            return false
         } 
     }
  } else {
    return false
  }
  return true
}

# Logic 2: Use net library and method ParseIP

// Add logic for leading zero case
import (
    "net"
)

func Is_valid_ip(ip string) bool {
  result := net.ParseIP(ip)
  if result != nil {
      return true
  }
	return false
}

# Logic 3: Regex compile the string
