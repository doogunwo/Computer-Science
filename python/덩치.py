
man = []
result = [] 
n = int(input())
for i in range(int(n)):
        weight, height = man(int,input().split())
        man.append((weight,height))
    
for i in man:
        rank = 1
        for j in man:
            if i[0] < j[0]   and i[1] < j[1] :
                rank = rank +1
        print(rank,end=' ')