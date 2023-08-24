package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
)

func message(conn net.Conn) {
	defer conn.Close()
	buffer := make([]byte, 1024)

	for {
		n, err := conn.Read(buffer)
		if err != nil {
			fmt.Println("연결 종료:", conn.RemoteAddr())
		}
		msg := string(buffer[:n])
		conn.Write([]byte(msg))
	}
}

func client() {
	fmt.Println("클라이언트실행")
	//소켓 생성
	connect, err := net.Dial("tcp", "127.0.0.1:1234")

	if err != nil {
		fmt.Println("서버 연결 실패:", err)
		return
	}

	defer connect.Close()

	fmt.Println("서버에 연결")
	reader := bufio.NewReader(os.Stdin)

	for {
		fmt.Println("나: ")
		msg, _ := reader.ReadString('\n')

		_, err := connect.Write([]byte(msg + "/n"))

		if err != nil {
			fmt.Println("메시지 전송 실패", err)
			return
		}

		buffer := make([]byte, 1024)
		n, err := connect.Read(buffer)

		if err != nil {
			fmt.Println("서버 응답 실패:", err)
			return
		}

		rcv := string(buffer[:n])
		fmt.Print(rcv)
	}

}

func server() {
	fmt.Println("서버실행")
	//소켓생성
	port := "1234"
	network := "tcp"

	//bind
	listener, err := net.Listen(network, ":"+port)
	if err != nil {
		fmt.Print("리스너 생성 실패", err)
		return
	}
	defer listener.Close()

	//listen()
	for {
		//accept()
		connect, err := listener.Accept()
		if err != nil {
			fmt.Println("연결 수락 실패", err)
			continue
		}
		//recv()
		fmt.Println("클라이언트 연결:", connect.RemoteAddr())
	}
}

func main() {
	fmt.Println("main")
	server()
}
