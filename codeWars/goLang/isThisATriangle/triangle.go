package kata

func IsTriangle(a, b, c int) bool {
    // Formula if the given sides form a triangle
    // Ref: https://www.wikihow.com/Determine-if-Three-Side-Lengths-Are-a-Triangle
    // * sum of any 2 sides is greater than the third side
    if a+b > c && a+c > b && b+c > a {
       return true
    }
    return false
}


