// Operators Challenge
// One Testcase failed with the logic. Rounding should be done proper
// Test3:
// Question: 10.25
//           17
//           5
// Without rounding the answer is 12.5099999.
// Answer: The total meal cost is 13 dollars.

package main
import (
    "fmt"
)

func main() {
    var mealCost float64;
    var tipPercent float64;
    var taxPercent float64;
    var answer int;
    fmt.Scanf("%f\n%f\n%f",&mealCost, &tipPercent, &taxPercent);
    tip := mealCost * (tipPercent/100);
    tax := mealCost * (taxPercent/100);
    if(float64(int(mealCost+tax+tip)) < mealCost+tax+tip) {
        if (mealCost+tax+tip > float64(int(mealCost+tax+tip))+0.50){
            answer = int(mealCost+tax+tip) + 1;
        } else {
            answer = int(mealCost+tax+tip);
        }
    } else {
        answer = int(mealCost+tax+tip);
    }
    fmt.Println("The total meal cost is",answer,"dollars.");
}
