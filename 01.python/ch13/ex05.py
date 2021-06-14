
def load(fpath):
    with open(fpath, 'rt', encoding='utf-8')as f:
        return f.readlines()


def convert(lines):       # 학생이름: key, 성적 리스트: value --> 사전을 리턴
    data = {}
    for line in lines[1:]:  # 헤더는 제외
        items = line.split(',')
        name = items[0]       # 이름
        scores = items[1:]    # 성적 리스트
        data[name] = list(map(int, scores))  # 사전에 추가
        # int를 통해\n삭제->white 문자(공백, 탭, 엔터)
    return data

# 저장하기
import pickle

def save(fpath,data):
    with open(fpath,'wb') as f:
        pickle.dump(data,f)

def main():   # 흐름제어
    try:
        lines = load('data.csv') # 밑에 두개가 대체 
        # fpath = input('파일명: ')  # 파일명 잘못 입력하면 예외 발생
        # lines = load(fpath)
        # print(lines)
        data = convert(lines)
        print(data)
        save('data.dat',data)

    except Exception as e:
        print('예외 발생', e)


main()

# 전역변수 사용 최대한 자제 버그발생 초래 찾기도 힘들다.
# 함수의 단일 책임이 중요
