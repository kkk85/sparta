def solution(num_list, n):
    return 1 if n in num_list else 0 # `num_list`에 숫자 `n`이 포함되어 있는 지 확인

# 입력
num_list = list(map(int, input("리스트를 입력하세요(공백으로 구분): ").split()))
n = int(input("정수: "))

# 결과 출력
result = solution(num_list, n)
print("결과:", result)
