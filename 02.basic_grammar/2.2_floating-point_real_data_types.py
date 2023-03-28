# 2.2 부동소수점 실수 자료형
# 정수와 실수 자료형
print(10) # 정수
print(10.0) # 실수
print(.1) # .1 = 0.1
print(10 * 5) # 정수
print(10.0 * 5) # 실수
print(10 / 5) # 실수

# 정수와 실수는 컴퓨터 메모리에 저장되는 방식이 다름 => 데이터의 자료형이 다르다라고 표현
# 실수는 float이라는 부동소수점(floating point number)자료형으로 처리

print(type(10))
print(type(10.0))

# 부동소수점 실수

# 프로그래밍 언어는 IEEE 754라는 국제표준에 따라 실수를 부동소수점 방식으로 표현
# 부동소수점 방식에서는 숫자를 정수로 된 유효숫자와 정수로 된 지수의 곱으로 표현
# 123.456 => 123456 x 10^-3
# 유효숫자e지수 = 유효숫자 x 10^지수

print(123e2)
print(123e-2)
print(123.456e-3)

# exercise 2.2.1
print(5e8)
print(5.6e3)
print(-2.1e2)
print(-3.4e-1)

# exercise 2.2.2
print(3141592e-6)
print(2718e-3)
print(14e-1)
print(173e-2)

# 십진법과 이진법
# exercise 2.2.3
print(1 * 10 ** 3 + 2 * 10 ** 2 + 3 * 10 ** 1 + 4 * 10 ** 0)
print(1 * 10 ** 3 + 0 * 10 ** 2 + 1 * 10 ** 1 + 0 * 10 ** 0)
print(3 * 10 ** 0 + 1 * 10 ** -1 + 4 * 10 ** -2)
print(2 * 10 ** -2 + 3 * 10 ** -3)

# exercise 2.2.4
print(bin(13))
print(bin(129))

# 부동소수점 오차
print(0.1 + 0.2 == 0.3)
print(round(0.1 + 0.2, 5) == round(0.3, 5)) # 연산 후 반올림한 뒤 반올림값과 비교
print(round((0.1 + 0.2) - 0.3, 5) == 0.0)

# 자료형 변환
print(int(1.0))
print(float(1))

# 정수형으로 변환하려는 숫자가 정확히 정수로 표현될 수 없으면 소숫점 이하의 숫자를 버린다.
print(int(3.14))
print(int(3.9))
print(int(-3.9))

# NaN과 Inf
# IEEE 754 표준에 따른 부동소수점 자료형은 특별한 두 가지 값을 표현할 수 있다.
# NaN(Not a Number) => 숫자가 아닌 것, Inf(Infinity) => 무한대
print(float("NaN"))
print(float("Inf"))
print(float("-Inf"))
