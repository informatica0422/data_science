# 정수 연산
print(1 + 1)
print(2 + 4 - 5)
print(2 * 4)
print(8 // 4) # 8을 4로 나눈 몫은 2
print(11 // 4) # 11을 4로 나눈 몫은 2
print(11 % 4) # 11을 4로 나눈 나머지는 3
print(10 / 4) # 10/4 = 2.5
print(2 ** 3) # 2의 세제곱은 8
print(2 ** -1) # 음수 제곱은 역수. 2^(-1) = 1/2
print(1000 ** 0) # 모든 수의 0제곱은 1

# exercise 2.1.1
print((3 * 2) - (8 / 4))
print(25 * 6 / 3 + 17)
print(39021 - 276920 / 12040)
print(2 ** 6 - 10 % 6)

# 연산 순서와 괄호
print(3 + 2 * 4)
print(3 + (2 * 4))
print((3 + 2) * 4)
print(100 / (3 * (10 - (3 * 2)) + 8))

# exercise 2.1.2
print(12 - (5 * 7 + 1))
print(5 * (8 + (10 - 6) / 2))
print(48320 - ((365 - 5 * 9) / 16) * 987)
print(((3 ** 4 - 3 * 7) % 5 + 4) ** 2)

# 부등식의 참과 거짓 계산
print(2 > 1)
print(2 > 2)
print(2 == 2)
print(2 != 1)
print(3 <= 3)

# exercise 2.1.3
print(3 == 3)
print(3 < 4)
print(3 != 4)
print(3 < 3)
print(2 > 3)
print(2 != 2)

# 부울리언 대수
print(True & True)
print(True & False)
print(False & True)
print(False & False)
print(True | True)
print(True | False)
print(False | True)
print(False | False)
print((2 > 0) & (2 < 3))
print((2 > 2) | (2 < 3))

# exercise 2.1.4
print((5 <= 6) & (3 == 4))
print((2 != 1) | (3 >= 4))
print((5 <= 6) & ((0 == 0) | (3 < 4)))

# 변수 사용하기
a = 2
b = 3
print(a * b)
a = 4
print((a > 0) & (a <= 10))

# exercise 2.1.5
for i in range(1,11):
    print(str(i) + "." + "(2 * " + str(i) + " - 1)^2 + 1 = " + str((2 * i - 1) ** 2 + 1))

    x = i
    y = i + 1
    z = 1 + 2

    print(str(i) + "." + str(x) + "^2*" + str(y) + " * (" + str(z) + " + 10) = " + str(x ** (2 * y) * (z + 10)))

    j = y
    k = z