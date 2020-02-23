# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트(순서o, 중복o, 수정o, 삭제o)
# 선언

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, d]
print(e)

# 인덱싱
print(d[3])
print(d[-2])  # 끝에서 순서로.
print(d[0] + d[1])
print(e[-1][3])  # Banana

# 슬라이싱
print(d[0:3])
print(e[2][1:3])  # 100, Pen
