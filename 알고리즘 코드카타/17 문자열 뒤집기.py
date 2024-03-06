def solution(my_string):
    return my_string[::-1] # 문자열을 저장하고 순서를 뒤집는다 (파이썬 슬라이싱)

# 문자열 입력 받기
input_string = input("문자열을 입력하세요: ")

# 결과 출력
result = solution(input_string)
print(f"뒤집힌 문자열: {result}")