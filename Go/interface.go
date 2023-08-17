//interface
//메서드들의 집합체
// 타입이 구현해야하는 메서드 원형들 정의
//탑 다운 방식의 구현을 위해서
//차상위 인터페이스 = 빈 인터페이스
//어떠한 타입도 담을 수 있는 컨테이너 = 동적 타입, 빈 인터페이스

package main

type Shape interface {
	area() float64
	perimeter() float64
}
