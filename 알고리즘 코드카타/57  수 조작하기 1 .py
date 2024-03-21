def solution(n, control):
    for index in control:
        if index == "w":
            n += 1 # w": 현재 숫자를 1 증가
        if index == "s":
            n -= 1 # "s": 현재 숫자를 1 감소
        if index == "d":
            n += 10 # "d": 현재 숫자를 10 증가
        if index == "a":
            n -= 10 # "a": 현재 숫자를 10 감소
    return n

n = int(input("초기 위치를 입력하세요: "))
control = input("이동 명령어를 입력하세요 (w, s, a, d로 이루어진 문자열): ").strip()

result = solution(n, control)
print("결과:", result)
