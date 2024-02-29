class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f"회원님의 이름: {self.name} 아이디: {self.username}")

    def __repr__(self):
        return f"{self.name}님의 회원정보 - 아이디: {self.username}"


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __repr__(self):
        return f"{self.author} 작성 : {self.title}  {self.content}"

members = []

m1 = Member('김용현', 'QWER', '1234')
m2 = Member('김도현', 'ASDF', '5678')
m3 = Member('김근동', 'ZXCV', '9012')
members.append(m1)
members.append(m2)
members.append(m3)

posts = []

for member in members:
    print(member.name)

p1 = Post('이게 1번이고', '1번입니다.', m1.name)
p2 = Post('이게 2번이고', '2번입니다.', m1.name)
p3 = Post('이게 3번이고', '3번입니다.', m1.name)
posts.append(p1)
posts.append(p2)
posts.append(p3)

p4 = Post('이게 4번이고', '4번입니다.', m2.name)
p5 = Post('이게 5번이고', '5번입니다.', m2.name)
p6 = Post('이게 6번이고', '6번입니다.', m2.name)
posts.append(p4)
posts.append(p5)
posts.append(p6)

p7 = Post('이게 7번이고', '7번입니다.', m3.name)
p8 = Post('이게 8번이고', '8번입니다.', m3.name)
p9 = Post('이게 9번이고', '9번입니다.', m3.name)
posts.append(p7)
posts.append(p8)
posts.append(p9)

print(posts)

while True:
    print("\n1. 회원 추가")
    print("2. 게시물 추가")
    print("3. 회원 리스트 보기")
    print("4. 게시물 리스트 보기")
    print("5. 종료")

    choice = input("번호를 선택하세요:")

    if choice == '1':
        name = input("이름을 입력하세요: ")
        username = input("아이디를 입력하세요: ")
        password = input("비밀번호를 입력하세요: ")

        new_member = Member(name, username, password)
        members.append(new_member)

        print(f"{name}님의 회원 정보가 추가되었습니다.")
    elif choice == '2':
        if not members:
            print("회원이 없습니다. 먼저 회원을 추가하세요.")
        else:
            for i, member in enumerate(members, start=1):
                print(f"{i}. {member.name}")

            member_index = int(input("게시물을 추가할 회원을 선택하세요 (번호): ")) - 1

            title = input("게시물의 제목을 입력하세요: ")
            content = input("게시물의 내용을 입력하세요: ")

            new_post = Post(title, content, members[member_index].name)
            posts.append(new_post)

            print(f"{members[member_index].name}님의 게시물이 추가되었습니다.")
    elif choice == '3':
        print("\n===== 회원 리스트 =====")
        for member in members:
            print(member)
    elif choice == '4':
        print("\n===== 게시물 리스트 =====")
        for post in posts:
            print(post)
    elif choice == '5':
        print("프로그램을 종료합니다.")
        break
    else:
        print("올바른 선택이 아닙니다. 다시 선택해주세요.")