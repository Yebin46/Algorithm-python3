from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for menu_num in course: # menu_num: 2, 3, 4, ...
        menu_combinations = [] # 나올 수 있는 모든 메뉴 조합 계산
        for order in orders: # order: "ABCFG"
            menu_combinations += combinations(sorted(order), menu_num)
        order_freq_dict = Counter(menu_combinations).most_common() # 빈도수 큰 순으로 '값':개수 반환
        answer += [key for key, value in order_freq_dict if value >= 2 and value == order_freq_dict[0][1]] # 가장 많이 주문 한 게 맨 앞

    answer = [''.join(course_comb) for course_comb in sorted(answer)]
    return answer

'''
order_freq_dict에서 index가 0인 것을 뽑는 게 아니라
value == order_freq_dict[0][1]를 쓰는 이유는 빈도수가 같은 경우가 있기 때문
'''