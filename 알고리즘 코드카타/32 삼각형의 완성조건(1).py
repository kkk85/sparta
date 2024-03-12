def solution(sides):
    sides.sort(reverse=True) # 리스트를 내림차순으로 정렬

    if sides[0] < sides[1] + sides[2]: # 조건문, 가장 긴 길이가 나머지 두 길이의 합보다 작으면 참이고 아니면 거짓이다.
        return "삼각형을 완성할 수 있습니다."
    else:
        return "삼각형을 완성할 수 없습니다."

# 입력
sides_input = []
for i in range(3):
    side = int(input(f"{i + 1}번째 변의 길이를 입력하세요: "))
    sides_input.append(side)

# 함수 호출 및 결과 출력
result = solution(sides_input)
print(result)
