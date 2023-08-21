package main

import (
	"fmt"
)

func printSlice(s string, x []int) {
	fmt.Println("%s len=%d cap=%d %v\n", s, len(x), cap(x), x)
}
func f1() {
	a := make([]int, 5)
	fmt.Println("hi f1")
	b := make([]int, 0, 5)

	fmt.Println(a)
	fmt.Println(b)
	printSlice("b", b)

}
