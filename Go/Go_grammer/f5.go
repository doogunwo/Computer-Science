package main

import (
	"encoding/json"
	"fmt"
	"log"
)

type Task struct {
	Title  string
	Status status
}
type status int // status == int

const (
	UNKNOWN status = iota // 0
	TODO                  // 1
	DONE                  // 2
)

func task_marshall() {

	t := Task{
		"Loundry",
		DONE,
	}
	b, err := json.Marshal(t)
	if err != nil {
		log.Println(err)
		return
	}
	fmt.Println(string(b))

}

func task_unmarshall() {
	b := []byte(`{"title":"Buy Milk","status":2`)
	t := Task{}

	err := json.Unmarshal(b, &t)

	if err != nil {
		log.Println(err)
		return
	}

	fmt.Println(t.Title)
	fmt.Println(t.Status)

}
