# 1 2 3 4 5
# 2 1 2 3 2 4 2 5
# 3 3 1 1 2 2 4 4 5 5
def solution(answers):
    
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    
  
    for i in range(len(answers)):
        
     
        if supo1[i%len(supo1)] == answers[i]:
            score[0] +=1
        if supo2[i%len(supo2)] == answers[i]:
            score[1] +=1
        if supo3[i%len(supo3)] == answers[i]:
            score[2] +=1
    ans = []
    for idx,num in enumerate(score):
        if num == max(score):
            ans.append(idx+1)
        
    return ans
answers = [1,3,4,5,2,3,4,5,6,3,5,6]

solution(answers)