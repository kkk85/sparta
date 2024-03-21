def solution(num_list):
    even_str = "" # 짝수
    odd_str = "" # 홀수

    for num in num_list:
        if num % 2 == 0:# 현재 숫자 짝수인지 판별
            even_str += str(num) # 짝수인 경우`even_str`에 더한다
        else:# 홀수인 경우
            odd_str += str(num) # 위와 똑같다.

    answer = int(even_str) + int(odd_str) # 짝수와 홀수를 나눠 저장한 문자열을 정수로 변환 그리고 두 값을 더한다.

    return answer

#  숫자 리스트 입력
num_list_input = list(map(int, input("숫자 리스트를 입력하세요 (공백으로 구분): ").split()))

# 결과 출력
result = solution(num_list_input)
print("결과:", result)