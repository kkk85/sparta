def solution(angle):
    if 0 < angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3
    elif angle == 180:
        return 4
    else:
        return 0  # 입력 범위를 벗어날 경우 반환 (0~180)

# 각도 입력
try:
    angle = float(input("각도를 입력하세요: "))

    # 결과 출력
    result = solution(angle)
    if result != 0:
        print(f"입력한 각도 {angle}는 {result}입니다.")
    else:
        print("올바른 각도를 입력하세요 (0에서 180 사이).")

except ValueError: # 예외
    print("올바른 숫자를 입력하세요.")
