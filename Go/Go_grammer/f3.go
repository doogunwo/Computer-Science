package main

import (
	"fmt"
)

func f3() {
	fmt.Println("hi4")

	var m map[int]string

	m = make(map[int]string)

	m[901] = "apple"
	m[134] = "grape"
	m[777] = "charile"

	myMap := map[string]string{
		"a": "Apple",
		"b": "banana",
		"c": "doogunwo",
	}
	for key, val := range myMap {
		fmt.Println(key, val)
	}
}
