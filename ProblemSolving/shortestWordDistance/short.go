func shortestDistance(words []string, word1 string, word2 string) int {
    // Logic 1: Naive O(N) - 100% fast
    n := len(words)
    var index1 int
    var index2 int
    shortest := 65535
    for i:=0;i<n;i++ {
        if words[i] == word1 {
            //index1 = append(index1, i)
            index1 = i+1
        } else if words[i] == word2 {
            //index2 = append(index2, i)
            index2 = i+1
        }
        //fmt.Println(index1, index2, shortest)
        if index1 > 0 && index2 > 0 {
            if index1-index2 > 0 && index1-index2 < shortest {
                shortest = index1 - index2
            }
            if index2-index1 > 0 && index2-index1 < shortest {
                shortest = index2 -index1
            }
        }
    }
    return shortest
}
