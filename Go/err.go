package main

import (
	"fmt"
	"log"
	"os"
)

func fopen() {
	f, err := os.Open("go.mod")

	if err != nil {
		log.Fatal(err.Error())
	}
	fmt.Println(f.Name())
}
