# 함수(function)는 입력을 받아 그 입력에 해당하는 출력을 반환(return)하는 기계와 같다.
# 파이썬에는 def 키워드와 return 키워드를 사용하여 다음과 같이 함수를 만들 수 있다.
# def 함수이름(입력변수이름):
#   출력변수를 만드는 명령
#   return 출력변수이름

def twotimes(x):
    y = 2 * x
    return y

print(twotimes(2))
print(twotimes(10))

def number(number):
    if number % 2 == 0:
        print("짝수입니다.")
    else:
        print("홀수입니다.")

number(9)

def year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("윤년입니다.")
            else:
                print("평년입니다.")
        else:
            print("윤년입니다.")
    else:
        print("평년입니다.")

year(2004)

def days1(month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        print(31)
    elif month == 2:
        print(28)
    else:
        print(30)

days1(2)

# 함수의 입력은 한 개가 아니라 여러 개가 되어도 상관없다.
# 입력 변수가 여러개이면 쉼표, 영어로 commma를 사용하여 함수를 정의한다.

def add(x, y):
    return x + y

print(add(1, 2))

def sum(a, b, c):
    s = a + b + c
    return s

print(sum(1, 2, 3))

def days2(year, month):
    year_finder = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                year_finder = True
            else:
                year_finder = False
        else:
            year_finder = True
    else:
        year_finder = False

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        print(31)
    elif month == 2:
        if year_finder:
            print(29)
        else:
            print(28)
    else:
        print(30)   

days2(2005,2)

# 람다 함수
# 함수에 이름을 주지 않거나 코드를 짧게 줄여쓰는 방법으로 람다(lambda)함수라는 것이 있다.
# 람다 함수는 함수 자체를 다른 함수의 인수로 넣을 때, 함수의 출력값을 함수로 받을 때 유용하게 사용된다.
f = lambda x : 2 * x

print(f(2))

m = 0

def diffsum(x, y, z):
    sum = x + y + z
    sum2 = (x ** 2) + (y ** 2) + (z ** 2)
    return sum2 - sum

print(diffsum(1, 2, 3))