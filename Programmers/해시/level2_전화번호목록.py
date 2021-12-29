def solution(phone_book):
    answer = True
    phone_book.sort()

    for idx in range(len(phone_book)):
        pre = phone_book[idx]
        if pre == phone_book[idx+1][:len(pre)]:
            return False
        if idx+1 == len(phone_book)-1:
            break
    return answer


'''
# 효율성 실패 -> 시간 복잡도 고려하기

def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for idx in range(len(phone_book)):
        pre = phone_book[idx]
        check_book = phone_book[:idx]+phone_book[idx+1:]
        for phone_num in check_book:
            if pre > phone_num:
                continue
            elif phone_num[:len(pre)] == pre:
                return False
    return answer
'''