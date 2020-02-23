# Section04-2
# 문자열, 문자열연산, 슬라이싱

str1 = 'I am Boy'
str2 = 'Jell'
str3 = ''
str4 = str()

print(len(str1), len(str2), len(str3), len(str4))

escape_str1 = 'Do you have a \'big collection\''
print(escape_str1)
escape_str2 = 'Tab\tTab\tTab'
print(escape_str2)


# Raw String
raw_s1 = r'C:\Program files\Test\Bin'  # escape가 먹히지 않음.
print(raw_s1)

raw_s2 = r'\\a\\a'  # escape가 먹히지 않음.
print(raw_s2)

# 멀티라인, \는 뒤에 변수가 있다고 파이썬 인터프리터에게 알려주는 역할.
multi = \
    '''
hihi

test
'''

print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = 'def'
str_o4 = 'jellive'


print(str_o1 * 100)
print(str_o2 + str_o3)
print(str_o1 + '3')
print('e' in str_o4)  # include와 같음.
print('z' not in str_o4)  # !include와 같음.

# 문자열 형 변환
print(str(77) + 'a')  # 숫자형 타입으로 하면 에러가 나지만 여기서는 안남.
print(str(10.4))


# 문자열 함수

# a = 'jell'
# b = 'orange'

# print(a.islower())  # True
# print(a.endswith('s'))  # False
# print(a.capitalize())  # 첫 글자만 대문자로 바꿔 줌.
# print(a.replace('e', 'ee'))
# print(list(reversed(b)))  # list로 형변환을 해줘야 함. 아니면 메모리만 나옴.


a = 'jell'
b = 'orange'

print(a[0:3])  # jel
print(a[:4])
print(a[0:len(a)])
print(a[:])
print(b[0:4:2])  # oa
print(b[1:-2])  # ran
print(b[::-1])  # egnaro, 즉 세 번째 파라미터는 for문의 마지막 같은 느낌으로..
