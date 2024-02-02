package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {

	var T, N int
	fmt.Scan(&T)

	results := make([]string, T)
	scanner := bufio.NewScanner(os.Stdin)
	for testCase := 1; testCase <= T; testCase++ {

		fmt.Scan((&N))
		//배열 1개 선언
		cards := make([]string, N)

		for j := 0; j < N; j++ {
			scanner.Scan()
			cards[j] = scanner.Text()
		}

		cost := 0

		for j := 1; j < N; j++ {

			if cards[j] < cards[j-1] {
				cost = cost + 1
				sort.Slice(cards[:j+1], func(j, k int) bool {
					return cards[j] < cards[k]
				})
			}
			//output[t - 1] = "Case #" + to_string(t) + ": " + to_string(cost);
		}

		results[testCase-1] = "Case #" + fmt.Sprint(testCase) + ": " + fmt.Sprint(cost)
	}

	for output := 0; output < T; output++ {
		fmt.Println(results[output])
	}

}
