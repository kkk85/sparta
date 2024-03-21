def solution(my_string, n):
    return my_string[:n] # 첫 번째 문자부터 n-1번째 문자를 추출

# 문자열과 n 입력
my_string_input = input("문자열을 입력하세요: ")
n_input = int(input("앞에서 몇 번째글자수까지: "))

# 결과 출력
result = solution(my_string_input, n_input)
print("결과:", result)
