def solution(array, n):
    answer = 0
    for num in array: # 리스트 순회
        if n == num: # num과 n가 같은지 비교
            answer += 1 # 같다면 answer +1
    return answer

# 리스트와 숫자 입력 받기
numbers = list(map(int, input("숫자 리스트를 입력하세요 (숫자 사이에 공백을 두고): ").split()))
target_number = int(input("찾을 숫자를 입력하세요: "))

# 결과 출력
result = solution(numbers, target_number)
print(f"{target_number}가 리스트에 {result}번 등장합니다.")
