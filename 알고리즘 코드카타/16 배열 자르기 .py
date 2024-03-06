def solution(numbers, num1, num2):
    answer = numbers[num1:num2+1] # numbers에서 num1, num2 부분 리스트 생성
    return answer

# 리스트와 인덱스 입력 받기
numbers_list = list(map(int, input("숫자 리스트를 입력하세요 (숫자 사이에 공백을 두고): ").split()))
start_index = int(input("시작 인덱스를 입력하세요: "))
end_index = int(input("끝 인덱스를 입력하세요: "))

# 결과 출력
result = solution(numbers_list, start_index, end_index)
print(f"부분 리스트: {result}")
