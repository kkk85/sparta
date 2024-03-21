def solution(my_string, k):
    answer = ""
    for i in range(k):
        answer += my_string
    return answer

# 입력
my_string = input("문자열을 입력하세요: ")
k = int(input("반복 횟수: "))

# 결과 출력
result = solution(my_string, k)
print("결과:", result)