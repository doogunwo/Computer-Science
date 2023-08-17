package main

import "fmt"

type Rect struct {
	width, height int
}

func (r Rect) area() int {
	r.width++
	return r.width * r.height
}

func (r *Rect) area2() int {
	r.width++
	return r.width * r.height
}

func obj() {
	rect := Rect{10, 20}

	area1 := rect.area()
	fmt.Println(rect.width, area1)

	area2 := rect.area2()
	fmt.Println(rect.width, area2)
}
