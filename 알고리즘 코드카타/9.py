def classify_angle(angle):
    if 0 < angle < 90:
        return "예각"
    elif angle == 90:
        return "직각"
    elif 90 < angle < 180:
        return "둔각"
    elif angle == 180:
        return "평각"
    else:
        return "올바른 각도를 입력하세요 (0에서 180 사이)."

# 각도 입력
try:
    angle = float(input("각도를 입력하세요: "))

    # 결과 출력
    result = classify_angle(angle)
    print(f"입력한 각도 {angle}은 {result}입니다.")

except ValueError:
    print("올바른 숫자를 입력하세요.")
