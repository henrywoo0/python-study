print(10 > 5) # True
print(10 < 3) # False
print(10 > 5 or 10 < 3)  # True   ||
print(10 > 5 and 10 < 3) # False &&
print(not True) # False
print(not True and True) # False
print(not True or True) # True
name = input('이름을 입력하세요')
print("my name is", name) # , 하면 자동으로 한칸 띄어쓰기
print("my name is"+name) # + 하면 그냥 더해서 나온다

# 입력
a = input('a=')
b = input('b=')
a = int(a)
b = int(b)
print('-'*30)
print(a+b)
print('-'*30)
a = int(input('a='))

# 사칙연산
a = int(input('a='))
b = int(input('b='))
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# 함수
def Hello():
    print('Hello')
    print('kim')

# 파이썬에서는 {}로 함수범위를 구분하지 않는다
# 대신 들여쓰기로 코드의 각 영역을 구분한다

def Hello1(name):
    print('Hi', name)

def Hello2(name):
    print(f'Hi {name}')

Hello1('준성')
Hello2('준성')

# 함수의 매개변수 사용해보기

def Hello3(name):
    print('Hi', name)

Hello3('whitebear')

def Hello4(name):
    print(f'hello, {name}') # f-string 방식으로 출력, f 접두사
    # python 3.6 version 이상

Hello4('JS')


def Hello5(name, hobby):
    print(f'Hi, My name is {name},' \
          f' My hobby is {hobby}')
    # 여러줄 연결 (\)

Hello5('whitebear', 'playing guitar')

# 매개변수로 넘긴 문자열 3개를 출력하는 프로그램 만들기

def info(name,age,hobby):
    print(f'제 이름은 {name}이고 나이는 {age}입니다.'\
          f'제 취미는 {hobby}에요')

info('whitebear','17','코딩')

# Hello() 함수에 'Kim'과 18이라는 매개변수 값을 넘겨줄때
# 'Hi,Kim,you are 18 years old.'이 출력되도록 하시오

def Hello(name,age):
    print(f'Hi,{name}, You are {age} years old.')

Hello('Kim',18)

# [문제] 자신이 좋아하는 가수 이름을 3개 입력(input()) 받고, 출력하는 함수 만들기
# 함수 이름 : singer(a,b,c)

def singer(a, b, c):
    print(f'내가 좋아하는 가수 {a},{b},{c}입니다.')

a = input('좋아하는 첫번째 가수 : ')
b = input('좋아하는 두번째 가수 : ')
c = input('좋아하는 세번째 가수 : ')
singer(a, b, c)

# [문제] 두 수를 입력받아 덧셈을 출력하도록 하시오.
# [입력] 4 7
# [출력] 11

n1=int(input()) # 이 방법으로는 4와 7을 한 줄에 입력받을 수 없음
n2=int(input())
print(n1+n2)

n1, n2 = map(int, input().split()) # map은 리스트의 요소를 지정된 함수로 처리해주는 함수
print(n1, n2)

# [문제] 두 수를 입력받아 SWAP하여 출력하시오.
# [입력] 9 7
# [출력] 7 9

n1, n2 = map(int, input().split())
n1, n2 = n2, n1 # 두 변수의 값을 교환
print(n1, n2)

# 제어문 : if문
a = 5
if a >= 3:
    print('3 이상')
elif a > 1: # else if
    print('3 미만 1 초과')
else:
    print('1 이하')

# [문제] 두 숫자를 한 줄에 입력받아 더 큰 수를 출력하는 프로그램을 만드시오
# [입력] 8 3
# [출력] 8

a, b = map(int, input().split())
if a > b:
    print(a)
else:
    print(b)

# [문제] 숫자를 하나 입력받아 70점 이상이면 '최우수'
# 그 외 50점 이상이면 '우수'
# 그 외 20점 이상이면 '보통'
# 그 외는 '노력 필요'를 출력하는 프로그램을 만드시오.

score = input()
if score >= 70:
    print('최우수')
elif score >= 50:
    print('우수')
elif score >= 20:
    print('보통')
else:
    print('노력 필요')

# [문제] 리스트에 주어진 알파벳을 오름차순으로 정렬하라
arr = ['b', 'c', 'd', 'f', 't', 'e']
arr.sort()
print(arr)

print(len(arr))

# [문제] 리스트 요소 중 아스키코드 값이 가장 큰 알파벳을 출력하시오.
arr = ['b', 'c', 'd', 'f', 't', 'e']
arr.sort(reverse=True) # 내림차순으로 정렬
print(arr[0])
# arr.sort() 했을 때 아래의 방식들로 쓸 수 있음
# print(arr[len(arr) - 1])
# print(arr[-1])

# [문제] 주어진 함수 리스트에서 최고점과 최저점을 출력하시오.
score = [55, 78, 99, 34, 87]
score.sort()
print(score[-1], score[0])
# print(max(score), min(score))


# for문
for i in range(10): # 0 ~ 9, range(0, 10)
    # print(i)
    print(i, end=' ')

# [문제] 1에서 100이하까지 홀수를 한 줄로 출력하시오.
for i in range(1, 101):
    if i % 2:
        print(i, end=' ')
