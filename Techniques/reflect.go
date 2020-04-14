// Reflect
package main;

import (
    "fmt"
    "reflect"
)

const (
  Cust  = iota
  Staff
)

type Office struct {
    Cust    Record
    Staff   Record
}

type Record struct {
  fname string
  lname string
}

func main() {
  downtown := Office{
    Cust: Record{
      fname: "Foo",
      lname: "Bar",
      },
    Staff: Record{
      fname: "Boo",
      lname: "Bee",
    },
  }
  fmt.Println(downtown)
  value := reflect.ValueOf(&downtown).Elem().Field(Cust)
  new_record := Record{
      fname: "Fam",
      lname: "Bat",
      }
  value.Set(reflect.ValueOf(new_record))
  fmt.Println(downtown)
}

