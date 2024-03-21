def solution(num_list, n):
    answer = []
    answer = num_list[:n] # 리스트 `num_list`를 `n` 대입
    return answer

# 입력
user_input = input("숫자 리스트를 공백으로 구분하여 입력하세요: ")
num_list = list(map(int, user_input.split()))

# 다른 입력값인 n을 받기
n = int(input("추출할 요소의 개수를 입력하세요: "))

# 결과 출력
result = solution(num_list, n)
print("결과:", result)
