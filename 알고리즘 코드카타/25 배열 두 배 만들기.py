def solution(numbers):
    return [num * 2 for num in numbers] # numbers리스트에서  입력 숫자 num * 2 (곱하기 2)

#  숫자 리스트 입력 받기
try:
    numbers = list(map(int, input("숫자 리스트를 입력하세요 (공백으로 구분): ").split()))
    result = solution(numbers)
    print(f"결과: {result}")
except ValueError:
    print("올바른 숫자를 입력하세요.")
