def solution(phone_book):
    answer = True
    set_p = set(phone_book)
    for p in phone_book:
        for ph in range(1, len(p)):
            if p[:ph] in set_p:
                return False
    return answer