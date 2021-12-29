from collections import defaultdict

def solution(clothes):
    
    cloth_dict = defaultdict(int)
    for cloth in clothes:
        cloth_dict[cloth[1]] += 1

    all_list = cloth_dict.values()

    answer = 1    
    for number in all_list:
        answer = answer * (number+1) # 선택하지 않는 경우도 포함해서 +1
    answer -= 1 # 모두 선택하지 않는 경우만 제외
    return answer

'''
# 시간 초과
from collections import defaultdict
from itertools import combinations
from functools import reduce

def solution(clothes):
    answer = 0
    
    cloth_dict = defaultdict(int)
    for cloth in clothes:
        cloth_dict[cloth[1]] += 1

    all_list = cloth_dict.values()
    
    for i in range(1, len(all_list)+1):
        for num in combinations(all_list, i):
            answer += reduce(lambda x, y: x * y, num)
    return answer
'''