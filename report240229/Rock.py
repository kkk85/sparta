import random

def get_user_choice():
    user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ").lower()
    while user_choice not in ['가위', '바위', '보']:
        print("올바른 선택이 아닙니다. 다시 입력해주세요.")
        user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ").lower()
    return user_choice


def get_computer_choice():
    return random.choice(['가위', '바위', '보'])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "무승부"
    elif (
            (user_choice == '가위' and computer_choice == '보') or
            (user_choice == '바위' and computer_choice == '가위') or
            (user_choice == '보' and computer_choice == '바위')
    ):
        return "사용자 승리"
    else:
        return "컴퓨터 승리"


if __name__ == "__main__":
    user_wins = 0
    computer_wins = 0
    total_games = 0

    print("가위바위보 게임을 시작합니다.")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"사용자: {user_choice}, 컴퓨터: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(f"결과: {result}")

        if result == "사용자 승리":
            user_wins += 1
        elif result == "컴퓨터 승리":
            computer_wins += 1

        total_games += 1

        print(f"현재 승부: 사용자 {user_wins} 승, 컴퓨터 {computer_wins} 승")
        print(f"총 게임 횟수: {total_games}")

        play_again = input("다시 하시겠습니까? (y/n): ").lower()
        if play_again != 'y':
            break

    print("게임 종료")
