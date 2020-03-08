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

# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6)
y.sort()
y.reverse()
y.insert(2, 7)
print(y)
ex = [88, 77]
y.extend(ex)  # append도 됨. 단 append는 리스트 자체가 들어감. extend 는 배열을 단순 확장시키는 것.
print(y)

# 삭제: del, remove, pop
