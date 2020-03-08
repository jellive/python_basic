# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dict): key-value

a = {'name': 'Kim', 'Phone': '010-7777-7777', 'birth': 870214}
b = {0: 'Hello python', 1: 'Hello Coding'}
c = {'arr': [1, 2, 3, 4, 5]}

# print(type(a)) # <class 'dict'>
print(a['name'])
print(a.get('name'))
print(c.get('arr')[1:3])

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)

a['rank'] = [1, 3, 4]
a['rank2'] = (1, 2, 3,)
print(a)

# key, values, item
print(a.keys())
print(list(a.keys()))
print(list(a.values()))
print(list(a.items()))
