### Solution

package kata

import (
    "strings"
)

func DecodeMorse(morseCode string) string {
  var result string
  var temp string
  // Three spaces splits words
  words := strings.Split(morseCode, "   ")
  for i:=0; i<len(words); i++ {
      temp = ""
      // One space splits characters
      characters := strings.Split(words[i], " ") 
      for j:=0; j<len(characters); j++ {
          temp += MORSE_CODE[characters[j]]
      }
      result += temp
      result += " "
  }
  return strings.TrimSpace(result)
}

### Test

package kata_test

import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/kata"
)

var _ = Describe("Test Example", func() {
  It("Example from description", func(){
    Expect(DecodeMorse(".... . -.--   .--- ..- -.. .")).To(Equal("HEY JUDE"))
  })
})
