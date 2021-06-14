# # 주소록 앱 ---> 객체 지향적으로...

# 1. 문제 파악
# 2. 문제 해결을 위해 필요한 객체가 뭐냐?
# 2.1 어떤 정보를 다루느냐?
#   1) 이름, 이메일, 전화번호, 주소 -->주소록 정보
#   2) 설정 정보(파일명,encoding 방식..)
# 2.2 단위 데이터의 형태가 어떻게 되는가?
#   1) 하나의 주소록 정보 : 이름, 이메일, 전화번호, 주소 --> 단위 데이터
#   2) 설정 정보
# 2.3 데이터의 개수, 어떻게 관리할 것인가?
#   1) 주소록 정보 N개 --> 콜렉션
#   2) 설정 정보 1개 -> 단일 변수

from app_base import Application
from models import AddressBook
# 모델(Model) 객체
# Configuration 설정 정보 담당
# AddressBookEntry
# AddressBook

# 객체 지향 설계 원칙
# 1) SRP(Single Responsibility Principle): 단일 책임의 원칙
# 2) OC(Open Close Principle): 확장에는 열려 있고, 변화에는 닫혀있음을 의미
#                              기능에 대한 확장은 열려 있어야 한다. 하지만 변화에는 닫혀있어야 한다.

# CLI --> GUI

class AddressBookApp(Application):
    def __init__(self):
        super().__init__()
        self.addressbook = AddressBook()
        self.addressbook.load(self.config)

    def create_menu(self, menu):
        # 메뉴를 구성해야 합니다.
        # 밑에 self.print_book() 괄호 하면 리턴값을 넣겠다는거 실수많이함
        menu.add('목록', self.print_book)
        menu.add('상세보기', self.print_detail)
        menu.add('검색', self.search)
        menu.add('추가', self.add)
        menu.add('수정', self.update)
        menu.add('삭제', self.delete)
        self.menu.add('종료', self.exit)  # self.menu랑 menu 같다.

    # 검색방법: 키워드 검색...'길동'-->[홍길동,고길동]

    def search(self):
        keyword = input('검색어: ')
        result = self.addressbook.search(keyword)
        # result 출력
        print('='*50)
        print(f'검색결과 ({len(result)}건)')
        print('='*50)
        for index, entry in enumerate(result, 1):
            print(
                f'{index:02d}]{entry.name}: {entry.phone}, {entry.email}, {entry.addr}')
        print('-'*50)

    def print_book(self):
        print('='*50)
        print('주소록')
        print('='*50)
        for index, entry in enumerate(self.addressbook.book, 1):
            print(
                f'{index:02d}]{entry.name}: {entry.phone}, {entry.email}, {entry.addr}')
        print('-'*50)

    def print_detail(self):
        index = int(input('선택(번호): '))
        entry = self.addressbook.book[index-1]
        # entry 포멧팅 해서 출력
        print(f'이름: {entry.name}')
        print(f'전화번호: {entry.phone}')
        print(f'email: {entry.email}')
        print(f'주소: {entry.addr}')

    def add(self):
        print('새 주소록 항목 추가')
        name = input('이름: ')
        phone = input('전화번호: ')
        email = input('email: ')
        addr = input('주소: ')
        self.addressbook.add(name, phone, email, addr)

    def update(self):
        index = int(input('대상 선택(번호): '))
        entry = self.addressbook.book[index-1]
        print('주소록 항목 수정')
        name = input(f'이름({entry.name}):')
        if name.strip() == '':
            name = entry.name
        phone = input(f'전화번호({entry.phone}):')
        if phone.strip() == '':
            phone = entry.phone
        email = input(f'email({entry.email}):')
        if email.strip() == '':
            email = entry.email
        addr = input(f'주소({entry.addr}):')
        if addr.strip() == '':
            addr = entry.addr

        self.addressbook.update(index-1, name, phone, email, addr)

    def delete(self):
        index = int(input('대상 선택(번호): '))
        entry = self.addressbook.book[index-1]
        ans = input(f'{entry.name}을 삭제할까요? (Y/N)')
        if ans == 'y' or 'Y':
            self.addressbook.delete(index-1)

    def destroyed(self):
        self.addressbook.save(self.config)


def main():
    app = AddressBookApp()
    app.run()


main()


# 기존 방법: 절차 중심 --> Topdown
# OOP: 객체 지향 방법 --> Bottom up  작은부품부터 시작해서 조립해나가는 방식

# 주소록
# Application
#      Configuration
#      Menu
#          MenuItem
#      AddressBook
#          AddressBookEntry

# 일기장
#
