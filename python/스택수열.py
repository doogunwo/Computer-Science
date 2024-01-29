n = int(input())  # 수열의 길이
sequence = [int(input()) for _ in range(n)]  # 만들어야 하는 수열

stack = []  # 스택
result = []  # push와 pop 연산을 저장하는 리스트
current = 1  # 현재 push해야 할 숫자

for num in sequence:
    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1

    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        break
else:  # 반복문이 정상적으로 종료되면 결과 출력
    print('\n'.join(result))
