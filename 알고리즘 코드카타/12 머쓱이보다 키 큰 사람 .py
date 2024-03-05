def solution(array, height):
    answer = 0
    for num in array:
        if num > height:
            answer += 1
    return answer

# 리스트 입력
def input_list():
    while True:
        try:
            num_list = input("숫자를 입력하세요 (공백으로 구분): ").split()
            num_list = [int(num) for num in num_list]
            return num_list
        except ValueError:
            print("올바른 숫자를 입력하세요.")

# 높이(머쓱이) 입력
def input_height():
    while True:
        try:
            height = int(input("머쓱이 키를 입력하세요 (1 이상 200 이하): "))
            if 1 <= height <= 200:
                return height
            else:
                print("높이는 1 이상 200 이하여야 합니다.")
        except ValueError:
            print("올바른 숫자를 입력하세요.")

# 입력 받기
array = input_list()
height = input_height()

# 결과 출력
result = solution(array, height)
print(f"{height} 이상인 수의 개수: {result}")
