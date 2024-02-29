import random

def guessing():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input('숫자를 입력하세요: '))
            attempts += 1

            if guess == number:
                print(f'정답! {attempts}번 만에 맞추셨습니다.')
                break
            elif guess > number:
                print('더 작은 수')
            else:
                print('더 큰 수')

        except ValueError:
            print('1-100 중의 숫자를 입력하세요')
        except Exception as e:
            print(f'오류 발생: {e}')

    return attempts

if __name__ == "__main__":
    while True:
        attempts = guessing()

        restart = input('게임을 다시 시작하시겠습니까? (y/n): ')
        if restart.lower() != 'y':
            print('게임 종료. 다음에 또 봐요!')
            break
