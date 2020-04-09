import (
    "fmt"
)

// Logic 1: Using to create a char freq map for every string and use the map as key for another map to track similar anagrams ( implement something kind of like set intersection )
// Can we use map as key to another map?
/*
func convertStringToMap(s string) map[rune]int {
    charMap := make(map[rune]int)
    for _, ch := range s {
        charMap[ch] += 1
    }
    return charMap
}
*/

// Logic 2: Sort the characters of a string and use them as key to the main anagram map

func sortCharInString(s string) string {
    split := strings.Split(s, "")
    sort.Strings(split)
    return strings.Join(split, "")
}


func groupAnagrams(strs []string) [][]string {
    groups := make(map[string][]string)
    for _, s := range strs {
        //sMap := convertStringToMap(s)
        sortStr := sortCharInString(s)
        groups[sortStr] = append(groups[sortStr], s)
    }
    anagrams := [][]string{}
    for _, value := range groups {
        anagrams = append(anagrams, value)
    }
    return anagrams
}
