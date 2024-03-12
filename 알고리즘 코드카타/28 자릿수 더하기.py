def solution(n):
    answer = 0
    str_n = str(n) # 문자열을 `str_n`에 저장한다
    for digit in str_n: # `str_n` 숫자 반복
        answer += int(digit) # 각 문자열 합계 계산
    return answer

# 입력
try:
    n = int(input("숫자를 입력하세요: "))
    result = solution(n)
    print(f"각 자리 숫자의 합: {result}")
except ValueError:
    print("올바른 숫자를 입력하세요.")
