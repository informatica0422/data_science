# for 반복문
# for 카운터변수 in range(반복횟수):
#   반복해서 실행할 명령
# 이 때 반복횟수는 10, 100과 같은 양의 정수이어야 한다.
# 현재 몇 번째 반복인지를 알려주는 변수를 카운터 변수(counter variable)이라고 한다.
# 이름은 아무거나 쓸 수 있으나 주로 i 또는 j 라는 변수 이름을 자주 사용한다.\
'''
for i in range(10):
    print("=")

for i in range(10):
    print(i)

for i in range(10):
    print("=" + str(i) + "=")

for i in range(10):
    print("=" + str(i + 1) + "=")

for i in range(10):
    print("*" * (i + 1))

for i in range(10):
    j = 10
    print("*" * (j - i))

for i in range(19):
    j = 19
    if i >= 0 and i <= 9:
        print("*" * (i + 1))
    else:
        print("*" * (j - i))
'''
a = 11

for i in range(11):
    if i >= 0 and i <= 5:
        j = 5
        if i == 0:
            print((" " * (j - i)) + ("*"))
        else:
            print((" " * (j - i)) + ("*" * ((i + 1) * 2 - 1)))
    else:
        j = 5
        print((" " * (i - j)) + ("*" * (a - 2)))
        a = a - 2