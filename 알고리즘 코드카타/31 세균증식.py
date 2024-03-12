def solution(n, t):
    for i in range(1, t + 1): # 1부터 t까지 반복
        n *= 2 #  n 값을 2배
        print(f"{i}시간 후: {n}마리")

    return n

#  입력
n_value = int(input("초기 숫자를 입력하세요: "))
t_value = int(input("흐른 시간을 입력하세요: "))

# 결과 출력
result = solution(n_value, t_value)
print(f"{t_value}시간 후 마리수: {result}")
