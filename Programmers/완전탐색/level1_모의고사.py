def solution(answers):
    answer = []
    
    # p1은 1,2,3,4,5 반복
    # p2는 2,1,2,3,2,4,2,5 반복
    # p3은 3,3,1,1,2,2,4,4,5,5 반복
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    
    s1=0
    s2=0
    s3=0
    
    for ind, ans in enumerate(answers):
        if ans == p1[ind%5]:
            s1 += 1
        if ans == p2[ind%8]:
            s2 += 1
        if ans == p3[ind%10]:
            s3 += 1
            
    temp_list = [s1, s2, s3]
    answer = list(filter(lambda x: temp_list[x] == max(temp_list), range(3)))
    
    for i in range(len(answer)):
        answer[i] += 1
        
    return answer