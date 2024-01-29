package main

import (
	"fmt"
)

func main1717() {
	var n int
	var m int

	_, err := fmt.Scan(&n, &m)
	if err != nil {
		return
	}

	fmt.Println(n, m)
}
