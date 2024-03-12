def solution(n):
    if n % 2 == 0: # 짝수인 경우
        answer = list(range(1, n + 1, 2)) # 1부터 n까지 2씩 증가한다 홀수만
    else:
        answer = list(range(1, n + 1, 2))

    return answer


# 입력
try:
    n = int(input("정수를 입력하세요: "))

    # 결과 출력
    result = solution(n)
    print("결과:", result)

except ValueError:
    print("올바른 정수를 입력하세요.")
