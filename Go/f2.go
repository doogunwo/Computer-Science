package main

import (
	"fmt"
	s "strings"
)

var p = fmt.Println

func f5() {
	p("hi")
	p(s.Count("test", "t"))
	p(s.HasPrefix("test", "te"))
	p(s.HasSuffix("test", "st"))
	p(s.Index("test", "es"))
	p(s.Join([]string{"a", "b"}, "-"))
	p(s.Repeat("doogunwo", 5))
	p(s.Replace("foo", "o", "0", -1))
	p(s.Replace("foo", "o", "0", 1))
	p(s.Split("a-b-c-d-e", "-"))
	p(s.ToLower("TEST"))
	p(s.ToUpper("test"))
	p(len("Hello"))
	p("hello"[2])

}
