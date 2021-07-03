def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers)) # 문자열 리스트로 바꾸기
    numbers.sort(key=lambda x:x*3, reverse=True)
    answer = str(int(''.join(numbers)))
    return answer