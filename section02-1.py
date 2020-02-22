# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해

# 기본 출력
print('Hello world!')
print("Hello world!")
print("""Hello
world!""")
print('''Hello
world!''')

print()


# Seperator 옵션 사용

print('T', 'E', 'S', 'T', sep='')  # sep는 join과 같다.
print('2019', '02', '19', sep='-')  # 2019-02-19
print('jellive7', 'google.com', sep="@")  # jellive7@google.com


# end 옵션 사용

print('Welcome to', end=' ')  # 끝을 ''로 하겠다. 즉 lnrn으로 끝내지 않겠다.
print('the black paradise', end=' ')
print('piano notes')

print('test')


# format 사용 [], {}, ()

print('{} and {}'.format('hi', 'world'))  # hi and world
print("{0} and {1} and {0}".format('hi', 'world'))  # hi and world and hi
print('{a} are {b}'.format(b='You', a='best'))

# %s: 문자, %d: 정수, %f: 실수
print("%s's favorite number is %d" % ('Jell', 47))

# 6534.12만 나옴.
print("Test1: %5d, Price: %4.2f" % (776, 6534.123))
# 위에꺼와 같으나 키가 추가된 형태.
print("Test1: {0: 5d}, Price: {1: 4.2f}".format(123, 4567.89))
# 키를 따로 지정해준 형태.
print("Test1: {a: 5d}, Price: {b: 4.2f}".format(a=776, b=6534.123))

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
...

"""

print('\'you\'')
print("\"you\"")
