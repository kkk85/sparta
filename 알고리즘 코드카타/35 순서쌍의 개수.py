def solution(n):
    answer = 0

    for i in range(1, n + 1): # 숫자  1 ~ n 까지
        if n % i == 0: # `i`가 `n`에 나누어 떨어지는 값 확인
            answer += 1 # 떨어지는 값이라면 1 증가

    return answer


# 사용자로부터 정수 입력 받기
try:
    n = int(input("정수를 입력하세요: "))

    # 결과 출력
    result = solution(n)
    print("결과:", result)

except ValueError:
    print("올바른 정수를 입력하세요.")
