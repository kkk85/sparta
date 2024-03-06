def solution(x, y):
    dot = [x, y] # 좌표 리스트(`dot`)
    answer = 0
    # 조건문을 통한 좌표 위치 나누기
    if dot[0] > 0 and dot[1] > 0:
        answer = 1
    elif dot[0] < 0 and dot[1] > 0:
        answer = 2
    elif dot[0] < 0 and dot[1] < 0:
        answer = 3
    elif dot[0] > 0 and dot[1] < 0:
        answer = 4

    return answer

# 입력값
x = int(input("x 좌표를 입력하세요: "))
y = int(input("y 좌표를 입력하세요: "))

# 결과 출력
result = solution(x, y)
print(f"입력된 좌표 ({x}, {y})는 {result} 사분면에 속합니다.")
