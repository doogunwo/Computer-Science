from datetime import  datetime,timedelta
def solution(today, terms, pri):
    answer = []
    today =  datetime.strptime(today, "%Y.%m.%d")

    for i in range(len(pri)):

        target = pri[i].split(" ")
        time= datetime.strptime(target[0], "%Y.%m.%d")
        
        for k in terms:

            term = k.split(" ")
            delta = timedelta(days=int(term[1])*28)
            if term[0] == target[1] :
                #today <time+delta
                print(today,time+delta)
                
                date1 = datetime.strptime(str(today), "%Y-%m-%d %H:%M:%S")
                date2 = datetime.strptime(str(time+delta),"%Y-%m-%d %H:%M:%S")

                if date1 > date2:
                    answer.append(i+1)                   

    print(answer)
    return answer


today = "2022.05.19"
terms= ["A 6", "B 12", "C 3"]

pri = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

solution(today,terms,pri)