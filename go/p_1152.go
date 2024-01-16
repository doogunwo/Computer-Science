package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	// 한 줄을 입력으로 받음
	reader := bufio.NewReader(os.Stdin)
	line, _ := reader.ReadString('\n')

	// 문자열 양 끝의 공백 제거
	line = strings.TrimSpace(line)

	// 공백을 기준으로 단어들을 분리하여 배열로 만듦
	words := strings.Fields(line)

	// 배열의 길이, 즉 단어의 개수 출력
	fmt.Println(len(words))
}
