import (
    "strings"
    "fmt"
)

func maxNumberOfBalloons(text string) int {
    balloons := map[string]int{
        "b": 0,
        "a": 0,
        "l": 0,
        "o": 0,
        "n": 0,
    }
    counts := 0
    for _, ch := range text {
        char := string(ch)
        if strings.Contains("ban", char) {
            balloons[char] += 1
        } else if strings.Contains("lo", char) {
            balloons[char] += 1
        }
    }
    mini_ones := 0
    mini_twos := 0
    if balloons["b"] < balloons["a"] {
        mini_ones = balloons["b"]
    } else {
        mini_ones = balloons["a"]
    }
    if balloons["n"] < mini_ones {
        mini_ones = balloons["n"] 
    }
    if balloons["l"] < balloons["o"] {
        mini_twos = balloons["l"]
    } else {
        mini_twos = balloons["o"]
    }
    mini_twos /= 2
    if mini_ones < mini_twos {
        counts = mini_ones
    } else {
        counts = mini_twos
    }
    return counts
}

/*
for key, value := range balloons {
    if key == "l" || key == "o" {
        twos += value
    } else {
        ones += value
    }
}
twos = twos/2
if twos%2 != 0 {twos -= 1}
counts += (ones-(ones%3))/3
fmt.Println(counts, twos, balloons)
for twos < counts {
    counts -= 1
}
*/
