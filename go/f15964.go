package main

import "fmt"

func main5() {
	var a, b, result int
	_, err := fmt.Scan(&a, &b)

	if err != nil {
		return
	}

	result = (a + b) * (a - b)
	fmt.Println(result)
}
