def solution(num_list):
    sorted_list = sorted(num_list) # 리스트 정렬 함수
    return sorted_list[:5] # 리스트 내 5번까지
# 리스트 입력
num_list = list(map(int, input("리스트를 입력하세요(공백으로 구분): ").split()))

# 함수 호출 및 결과 출력
result = solution(num_list)
print("결과:", result)
