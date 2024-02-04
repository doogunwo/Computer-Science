n = int(input())  # 점의 개수 N을 입력받음
points = [tuple(map(int, input().split())) for _ in range(n)]  # 점의 좌표를 입력받아 리스트에 저장

# points 리스트를 정렬하는데, 람다 함수를 사용하여 정렬 기준을 x좌표, 그리고 x좌표가 같을 경우 y좌표로 설정
points.sort(key=lambda point: (point[0], point[1]))

# 정렬된 좌표를 출력
for x, y in points:
    print(x, y)
