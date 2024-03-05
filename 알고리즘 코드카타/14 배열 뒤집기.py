def solution(num_list):
    return num_list[::-1] # 리스트 뒤집어서 반환

# 리스트 입력
numbers = input("리스트를 입력하세요 (숫자 사이에 공백을 두고): ").split()
numbers = [int(num) for num in numbers]

# 결과 출력
result = solution(numbers)
print("뒤집힌 리스트:", result)
