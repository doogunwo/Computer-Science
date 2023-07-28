def solution(n, arr1, arr2):
    answer = []

    str3 = '0'+str(n)+'b'
    binary_list1 = [format(num, str3) for num in arr1]
    binary_list2 = [format(num, str3) for num in arr2]
 
    for i in range(n):
        
        k1 = list(binary_list1[i])
        k2 = list(binary_list2[i])
        mid = []
        for j in range(n):
            
            res = int(k1[j]) | int(k2[j])
            
            mid.append(res)
        answer.append(mid)
    out_1 = []
    for row in answer:
        out  = ''
        for ele in row:
            if ele ==1:
                out = out + "#"
            else:
                out = out + " "
        out_1.append(out)    
                
    
  
    
    return out_1

