// Logic 1: Naive way of using map and iteration with Sum of digits helper function - 100 pass - 60% faster
func sumOfDigits(n int) int {
    total := 0
    for n > 0 {
        total += n%10
        n = n/10
    }
    return total
}

func countLargestGroup(n int) int {
    // Track max group size
    max_group_size := 0
    // Map Sum to Digits
    dict := make(map[int][]int)
    // Iterate n
    for i:=1; i<=n; i++ {
        sumOfDigit := sumOfDigits(i)
        dict[sumOfDigit] = append(dict[sumOfDigit], i)
        if len(dict[sumOfDigit]) > max_group_size {
            max_group_size = len(dict[sumOfDigit])
        }
    }
    result := 0
    for _, value := range dict {
        if len(value) == max_group_size {
            result += 1
        }
    }
    //fmt.Println(dict, max_group_size)
    return result
}
