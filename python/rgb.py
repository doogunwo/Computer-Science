def min_cost_to_paint_houses(costs):
    if not costs:
        return 0

    n = len(costs)
    for i in range(1, n):
        costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
        costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
        costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])

    return min(costs[-1])

# 입력 예시
costs = [[26, 40, 83], [49, 60, 57], [13, 89, 99]]
result = min_cost_to_paint_houses(costs)
print(result)
