package main

import (
	"fmt"
)

func main2003() {
	var n, m int

	// n과 m 입력
	fmt.Scan(&n, &m)

	nums := make([]int, n)

	// 수열 입력
	for i := 0; i < n; i++ {
		fmt.Scan(&nums[i])
	}

	count := 0
	start, end, sum := 0, 0, 0

	// 투 포인터 알고리즘
	for start < n {
		if sum < m {
			if end == n {
				break
			}
			sum += nums[end]
			end++
		} else {
			sum -= nums[start]
			start++
		}

		if sum == m {
			count++
		}
	}

	println(count)
}
