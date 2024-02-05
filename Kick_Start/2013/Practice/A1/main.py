def calculate_sorting_cost(test_cases):
    results = []#결과
    for index, names in enumerate(test_cases, start=1):#
        cost = 0#비용 
        for i in range(1, len(names)):#
            if names[i] < names[i - 1]:  
                cost += 1
                names[:i + 1] = sorted(names[:i + 1]) 
        results.append(f"Case #{index}: {cost}")
    return results

# 메인부분
test_cases = []
T = int(input())

for i in range(T):

    n= int(input())
    case = [ input() for _ in range(n)]
    test_cases.append(case)


# 함수 호출
results = calculate_sorting_cost(test_cases)

# 결과 출력
for result in results:
    print(result)
