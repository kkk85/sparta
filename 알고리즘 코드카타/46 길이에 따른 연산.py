def solution(num_list):
    answer = 0

    # 길이가 11이상일 경우, 리스트 내 모든 수 더한다
    if len(num_list) >= 11:
        for num in num_list:
            answer += num
    # 길이가 11미만일 경우, 리스트 내 모든 숫자 곱한다
    else:
        answer = 1
        for num in num_list:
            answer *= num

    return answer

# 입력
num_list = list(map(int, input("여러 개의 숫자를 입력하세요 (공백으로 구분): ").split()))

# 결과 출력
result = solution(num_list)
print("결과:", result)
