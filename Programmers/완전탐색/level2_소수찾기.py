from itertools import permutations
from math import sqrt

def is_prime_number(x):
    if x == 1 or x == 0:
        return False
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    prime_number_list = []
    numbers_set = list(numbers)
    for num_len in range(1, len(numbers)+1):
        for candidate in permutations(numbers_set, num_len):
            candidate_number = int(''.join(candidate))
            # print(candidate_number)
            if is_prime_number(candidate_number):
                prime_number_list.append(candidate_number)
    answer = len(set(prime_number_list))
    return answer