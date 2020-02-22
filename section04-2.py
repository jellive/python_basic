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
