n,m = map(int,input().split())
nums = list(map(int,input().split()))

count = 0
start,end, sum =0,0,0

while start <len(nums):

    if sum < m:
        if end == len(nums):
            break
        sum = sum + nums[end]
        end = end +1
    
    else:
        sum = sum - nums[start]
        start = start +1
    
    if sum == m:
        count = count +1

print(count)