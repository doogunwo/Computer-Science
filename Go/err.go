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
	b1 := make([]byte, 50)
	_, err = f.Read(b1)
	fmt.Println(string(b1))
	fmt.Println(f.Name())
}
