def solution(n):
    if n % (n**0.5) == 0: # `n`의 제곱근으로 나눈 나머지가 0인지 아닌지에 따라 반환한다
        return 1  # 나누어 떨어진다
    else:
        return 2  # 안 떨어진다

#  숫자 입력
try:
    input_number = int(input("숫자를 입력하세요: "))
    result = solution(input_number)
    print(f"결과: {result}")
except ValueError:
    print("올바른 숫자를 입력하세요.")
