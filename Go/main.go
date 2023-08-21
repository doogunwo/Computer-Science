package main

import (
	"fmt"
)

func main() {
	var s1 string
	fmt.Scan(&s1)
	for i := 0; i < len(s1); i++ {
		fmt.Println(string(s1[i]))
	}

}
