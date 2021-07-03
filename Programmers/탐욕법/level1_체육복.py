def solution(n, lost, reserve):
    answer = 0
    
    lost.sort()
    reserve.sort()
    lost_cop = lost.copy()
    for lost_std in lost_cop: # 여벌을 가진 학생이 도난 당한 경우 다른 학생에게 빌려줄 수 없음
        if lost_std in reserve:
            answer += 1
            reserve.remove(lost_std)
            lost.remove(lost_std)
            
    for lost_std in lost:        
        if lost_std-1 in reserve: # 앞 번호 학생이 체육복 여분이 있는 경우
            answer += 1
            reserve.remove(lost_std-1)
        elif lost_std+1 in reserve: # 뒷 번호 학생이 체육복 여분이 있는 경우
            answer += 1
            reserve.remove(lost_std+1)
    
    for i in range(n-len(lost_cop)):
        answer += 1

    return answer