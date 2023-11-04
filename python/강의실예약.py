import sys

n, m = map(int, input().split())

using_class = []
result = []
for i in range(m):
    val = sys.stdin.readline().rstrip()  # sys.stdin.readline()로 읽은 문자열의 마지막 개행문자를 제거
    values = val.split()  # 공백으로 분할하여 리스트로 변환
    class_number = int(values[0])
    start_time = int(values[1])
    end_time = int(values[2])

    
    if(i==0):
        using_class.append([class_number,start_time,end_time])
        result.append("YES")
    if(i>0):
        using_class.append([class_number,start_time,end_time])

        if(using_class[i][0] != using_class[i-1][0]):
            #앞뒤 강의실이 맞지않을때는 YES
            result.append("YES")
        else:
            if using_class[i][1] < using_class[i-1][2]:
                result.append("NO")
            #다음 강의실 시간이 이전 강의실 시작시간보다 클때 

print(result)    

    
    

