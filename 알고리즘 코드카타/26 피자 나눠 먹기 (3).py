def solution(slice, n):
    answer = 0
    if n % slice == 0:
        answer = n // slice
    else:
        answer = n // slice + 1
    return answer

# 사용자로부터 입력 받기
try:
    slice_size = int(input("한 판에 몇 조각씩 자를지 입력하세요: "))
    total_slices = int(input("총 몇 조각의 피자가 필요한지 입력하세요: "))
    result = solution(slice_size, total_slices)
    print(f"{total_slices}명이 최소 한 조각씩 먹기 위해서 최소 {result}판이 필요합니다.")
except ValueError:
    print("올바른 숫자를 입력하세요.")
