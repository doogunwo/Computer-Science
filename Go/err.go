package main

import (
	"fmt"
	"log"
	"os"
)

func fopen() {
	f, err := os.Open("1.txt")

	if err != nil {
		log.Fatal(err.Error())
	}

	fmt.Println(f.Name())
}
