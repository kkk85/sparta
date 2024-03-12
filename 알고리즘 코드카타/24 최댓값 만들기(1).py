def solution(numbers):
    answer = 0
    max_product = 0

    for i in range(len(numbers)): # for문 루프로 리스트 내 모든 숫자 처음부터 끝까지 인덱스로 저장
        for j in range(i + 1, len(numbers)):
            if numbers[i] * numbers[j] > max_product: # 모든 곱을 합
                max_product = numbers[i] * numbers[j] # 결과값 업데이트

    answer = max_product
    return answer

# 숫자 리스트 입력
try:
    numbers = list(map(int, input("숫자 리스트를 입력하세요 (공백으로 구분): ").split()))
    result = solution(numbers)
    print(f"결과: {result}")
except ValueError:
    print("올바른 숫자를 입력하세요.")
