'''
정확도 100
효율성 0

-> 좀 더 효율적인 코드를 고려해보자
'''

def solution(info, query):
    answer = []
    for conditions in query:
        condition_list = conditions.replace(' and ', ' ').split()
        score = int(condition_list[-1])
        condition_list = condition_list[:-1] # 점수 제외 다른 조건들
        count = 0
                
        for applicant in info:
            app_list = applicant.split()
            a_score = int(app_list[-1])
            app_list = app_list[:-1]
            if a_score < score: # 기준 점수를 넘지 않으면
                continue # 다음 사람을 확인
            else: # 기준 점수를 넘으면
                for ind, condition in enumerate(condition_list): # 각 조건에 해당하는지 확인
                    if condition == '-' and ind != 3: # - 이면
                        continue # 다른 조건을 살핀다
                    elif condition == '-' and ind == 3:
                        pass
                    elif condition != app_list[ind]:
                        break # 조건에 부합하지 않으면 다음 사람을 확인
                    if ind == 3: # 모든 조건에 부합하면
                        count += 1 # 인원 추가
        answer.append(count)
        
    return answer