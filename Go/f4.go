package main

import (
	"fmt"
)

func say(msg ...string) {
	for _, s := range msg {
		fmt.Println(s)
	}
}
