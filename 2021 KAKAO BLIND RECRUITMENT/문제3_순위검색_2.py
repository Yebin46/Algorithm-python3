'''
정확도 100
효율성 100
'''

from bisect import bisect_left
from itertools import combinations

def all_cases(applicant):
    '''
    해당 지원자가 검색될 수 있는 모든 경우를 list로 return
    '''
    case_list = []
    for combi_num in range(5): # 0(아무것도 선택X),1,2,3,4
        # combi_num: 점수를 제외한 4개의 조건 중 몇 개의 조건을 선택?
        for combi in combinations([0, 1, 2, 3], combi_num):
            case = ''
            for condition_ind in range(4): # 0, 1, 2, 3
                if condition_ind not in combi:
                    case += applicant[condition_ind]
                else:
                    case += '-'
            case_list.append(case)
    return case_list


def solution(info, query):
    answer = []
    all_applicants = {} # dictionary

    for applicant in info:
        app_info = applicant.split()
        app_score = int(app_info[-1])
        case_list = all_cases(app_info)
        for case in case_list:
            if case not in all_applicants.keys(): # case를 key로, 점수를 value로 dictionary에 저장
                all_applicants[case] = [app_score]
            else: # 해당 case가 이미 있으면 점수만 append
                all_applicants[case].append(app_score)

    for key in all_applicants.keys():
        all_applicants[key].sort() # 점수 기준 오름차순 정렬

    for conditions in query:
        condition_list = conditions.replace(' and ', ' ').split()
        score = int(condition_list[-1])
        condition = ''.join(condition_list[:-1])
        if condition in all_applicants.keys():
            answer.append(len(all_applicants[condition]) - bisect_left(all_applicants[condition], score, lo=0, hi=len(all_applicants[condition])))
        else:
            answer.append(0)

    return answer



'''
다른 사람의 풀이 중 좋아보이는 풀이

def solution(info, query):
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    for k in data:
        data[k].sort()

        # print(k, data[k])

    answer = list()
    for q in query:
        q = q.split()

        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])
        l = 0
        r = len(pool)
        mid = 0
        while l < r:
            mid = (r+l)//2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid+1
            # print(l, r, mid, answer)
        # answer.append((pool, find, mid))
        answer.append(len(pool)-l)

    return answer
'''