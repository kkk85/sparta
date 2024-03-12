def solution(array):
    answer = 0

    array.sort() # 배열 오름차순 정렬
    index = len(array) // 2 # 배열 중앙 인덱스 값 구하기
    answer = array[index]  # 배열의 중앙값을 answer에 저장

    return answer

#  리스트 입력
try:
    input_list = list(map(int, input("숫자 리스트를 입력하세요 (공백으로 구분): ").split()))
    result = solution(input_list)

    # 결과 출력
    print(f"중앙값: {result}")
except ValueError:
    print("올바른 숫자 리스트를 입력하세요.")
