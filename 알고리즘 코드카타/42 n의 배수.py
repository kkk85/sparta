def solution(num, n):
    answer = 0  # 변수 초기화

    # 조건문 if문 `num`이 `n`으로 나눈다
    if num % n == 0:
        answer = 1 # n으로 나누어 떨어지면 1로 반환 (배수)
    else:
        answer = 0 # 아니라면 0으로 반환 (배수가 아님)

    return answer

# 입력 받기
num_input = int(input("num을 입력하세요: "))
n_input = int(input("n을 입력하세요: "))

# 결과 출력
result = solution(num_input, n_input)
print("결과:", result)
