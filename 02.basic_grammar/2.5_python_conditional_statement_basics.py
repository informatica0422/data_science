# if ~ else 명령
# "참 또는 거짓을 가지는 값"은 조건(condition)이라고 부른다.
# 참 또는 거짓일 때 실행되는 명령들은 빈칸을 4칸 띄우고 써야 한다. 이를 들여쓰기(indentation)라고 한다.
a = 10

if a % 2 == 0:
    print("짝수")
else:
    print("홀수")

b = 10

if (b >= 10) & (b < 100) & (b % 2 == 0):
    print("2자리 수의 짝수이다.")
else:
    print("2자리 수의 짝수가 아니다.")

y = 2009

if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print("윤년입니다.")
        else:
            print("평년입니다.")
    else:
        print("윤년입니다.")
else:
    print("평년입니다.")

# 조건으로 나누어야 할 경우의 수가 두 가지가 아니라 여러 가지일 때는 다음과 같이 명령을 사용할 수 있다.
# if ~ elif ~ else

c = 10

if c >= 8:
    print("A")
elif c >= 5:
    print("B")
else:
    print("C")

water = 9

if water >= 10:
    print("1등급")
elif water >= 7:
    print("2등급")
elif water >= 4:
    print("3등급")
else:
    print("4등급")

gender = "boy"
pushup = 8

if gender == "boy":
    if pushup >= 10:
        grade = "Pass"
    else:
        grade = "Fail"
else:
    if pushup >= 5:
        grade = "Pass"
    else:
        grade = "Fail"

print(grade)

xa = False
xb = False

if (xa == True) & (xb == False):
    ya = 0 
    yb = 10
elif (xa == False) & (xb == True):
    ya = 10
    yb = 0
elif (xa == True) & (xb == True):
    ya = 5
    yb = 5
else:
    ya = 1
    yb = 1

print(ya)
print(yb)