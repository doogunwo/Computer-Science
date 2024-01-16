package main

import (
    "bufio"
    "os"
    "strconv"
)

func main() {
    var n, m int
    io := bufio.NewReader(os.Stdin)

    // n과 m 입력
    io.Scan(&n, &m)

    nums := make([]int, n)

    // 수열 입력
    for i := 0; i < n; i++ {
        io.Scan(&nums[i])
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
