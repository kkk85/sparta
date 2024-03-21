def solution(num_list):

    # 리스트 내 합과 곱을 계산
    list_sum = sum(num_list)
    list_product = 1
    for num in num_list:
        list_product *= num

    #제곱과 곱을 비교하여 결과 설정
    if list_sum ** 2 > list_product:
        answer = 1
    else:
        answer = 0

    return answer

# 입력
input_list = list(map(int, input("숫자들을 공백으로 구분하여 입력하세요: ").split()))

# 결과 출력
result = solution(input_list)
print("합계:", sum(input_list))
print("결과:", result)
