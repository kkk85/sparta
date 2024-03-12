def solution(num_list):
    answer = [0, 0] # 리스트 초기화
    for num in num_list: # num_list 숫자 순회 (for문)
        if num % 2 == 0: # 홀수인지 짝수인지 따라 각 +1 카운트
            answer[0] += 1
        else:
            answer[1] += 1
    return answer

#  입력 받기
try:
    num_list_str = input("숫자 리스트를 입력하세요 (공백으로 구분): ")
    num_list = list(map(int, num_list_str.split()))
    result = solution(num_list)

    # 결과 출력
    print(f"짝수 개수: {result[0]}, 홀수 개수: {result[1]}")
except ValueError:
    print("올바른 숫자를 입력하세요.")
