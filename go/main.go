package main

import (
	"fmt"
	"bufio"
	"os"
)
// 0 A B => 합집합 
// 1 A B => 두원소가 같은 집합에 포함인지 
// N -> N+1개의 집합 0~N+1개
// M은 입력 수

var parent []int

func find(x int) int {
	if parent[x] == x{
		return x
	}
	parent[x] = find(parent[x])
	return parent[x]
}

func union(x,y int){
	xRoot := find(x)
	yRoot := find(y)

	if xRoot != yRoot {
		parent[yRoot] = xRoot
	}
}

func isSameSet(x,y int) bool {
	return find(x) == find(y)
}

func main(){
	
	var n,m int
	scanner := bufio.NewScanner(os.Stdin)
    scanner.Split(bufio.ScanWords)
    scanner.Scan()
    fmt.Sscan(scanner.Text(), &n)
    scanner.Scan()
    fmt.Sscan(scanner.Text(), &m)

	parent = make([]int, n+1)
	for i:= range parent {
		parent[i] =i
	}

	for i:=0; i<m; i++ {
		var cmd,a,b int
		scanner.Scan()
        fmt.Sscan(scanner.Text(), &cmd)
        scanner.Scan()
        fmt.Sscan(scanner.Text(), &a)
        scanner.Scan()
        fmt.Sscan(scanner.Text(), &b)

		if (cmd == 0) {
			union(a,b)
		} else if (cmd == 1){
			if (find(a) == find(b)) {
				fmt.Println("YES")
			} else {
				fmt.Println("NO")
			}
		}
	}
}