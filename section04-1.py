# 데이터 타입

import math
v_str1 = "Jell"
v_bool = True
v_str2 = "mystral"
v_float = 10.3
v_int = 7
v_dict = {
    "name": "Kim",
    "age": 25
}

v_list = [3, 5, 7]  # Array와 같음.

v_tuple = 3, 5, 7

v_set = {7, 8, 9}

print(type(v_tuple))
print(type(v_set))
print(type(v_float))
print(type(v_dict))

i1 = 39
i2 = 939
big_int1 = 99999999999999999999999999999999999999999999
big_int2 = 77777777777777777777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)
print(f3 + i2)

result = f3 + i2
print(result)
print(type(result))

a = 5.
b = 4

print(type(a), type(b))
result2 = a + b
print(result2)  # float

# 형변환
# int, float, complex(복소수)

print(int(result2))
print(complex(3))
print(int('3'))
print(complex(False))

y = 100
y *= y
print(y)

# 수치 연산 함수
# https://docs.python.org/3/library/math.html

print(abs(-7))  # 절대값
n, m = divmod(100, 8)  # 몫은 첫 번째, 나머지는 두 번째로 들어 감.
print(n, m)


print(math.ceil(-7.1))  # 올림
print(math.floor(3.874))  # 내림
