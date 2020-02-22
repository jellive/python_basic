# Section02-2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습

# import this # 이스터 에그.
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding)  # UTF-8
print(sys.stdout.encoding)  # UTF-8

# 출력문
print('My name is Goodboy!')

# 변수 선언
myName = 'Badboy'
print('My name is {name:s}!'.format(name=myName))

# 조건문
if myName == 'Goodboy':
    print('Ok')
else:
    print('myName is not \'Goodboy\'. myName is %s' % (myName))


# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d =' % (i, j), i*j)  # ,의 중요성

# 변수 선언(한글)
이름 = '좋은사람'
print('내 이름은 {}'.format(이름))


# 함수 선언


def 인사():
    print('안녕하세요, 반갑습니다.')


인사()


def greeting():
    print('Hello, nice to see you!')


greeting()

# 클래스


class Cookie:
    pass


# 객체 생성
cookie = Cookie()

print(id(cookie))  # 메모리 값인가?
print(dir(cookie))
