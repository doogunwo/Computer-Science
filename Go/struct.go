package main

import (
	"fmt"
)

type person struct {
	name string
	age  int
}

var P = fmt.Println

func struct_ex() {
	fmt.Println("struct_ex")
	p := person{}
	p.name = "dgw"
	p.age = 10

	p2 := person{name: "ddw", age: 50}
	p3 := new(person)
	p3.name = "ldld"

	P(p)
	P(p2)
	P(p3)

}
