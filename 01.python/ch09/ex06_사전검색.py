# find index는 함수 자체내에서 루프를 돌기 때문에 시간이 오래걸린다
# 하지만 사전은 키값을 해쉬값 즉 숫자로 가지고있어서 키값만 안다면
# 찾는시간을 극소화 시킬수있다.
song = """by the rivers of babylon, there we sat down
yeah we wept, when we remember zion.
when the wicked carried us away in captivity
required from us a song
now how shall we sing the lord's song in a strange land"""

alphabet = dict()
for c in song:
    if c.isalpha() == False:  # 부호, 개행문자는 제외하는 조건.
        continue
    c = c.lower()
    if c not in alphabet:  # 처음 등장한 경우.
        alphabet[c] = 1
    else:
        alphabet[c] += 1

print(alphabet)

# 알파벳 순서대로
key = list(alphabet.keys())
key.sort()
for c in key:
    num = alphabet[c]
    print(f'{c} : {num}')

# 벨류 높은 순
# 벨류가 높은 순서대로는 힘들다 벨류로 키를 찾을수가 없어서
# sort메소드 말고 items로 찾는다

def get_value(a):
    print(a)      # a[0] - key, a[1] - value / ('b', 4)
    return a[1]   # value

items = list(alphabet.items())
print(items)
items.sort(reverse=True, key=get_value) 
# items.sort(reverse=True, key=lambda a: a[1]) 이거 쓰면
# 함수정의 안하고 바로 할 수 있다. a[0] 이면 키 a[1]이면 벨류정렬

for k, v in items:
    print(f'{k} : {v}')

# 단어 횟수로 찾기

word_dict = {}  # dict()
# for line in song.splitlines: # 라인 단위 분리
lines = song.splitlines()

for line in lines:
    words = line.split()
    for word in words:     # 한 라인에서 단어 분리
        word = word.lower()
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

print(word_dict)
print(song.splitlines())
