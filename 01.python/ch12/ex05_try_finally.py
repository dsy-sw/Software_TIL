def chat():
    try:
        print('네트워크 접속')
        #a = 2/0
        return
        print('네트워크 통신 수행')
    except:
        print('네트워크 에러 발생')
    finally:
        print('접속 해제')

    print('=========================')


print('통신을 시작합니다.')
chat()
print('통신이 끝났습니다.')

# try except를 거쳐야 파이널이 실행됨 중요!!!
# 오류없어 except를 안거치면 finally 실행안됨