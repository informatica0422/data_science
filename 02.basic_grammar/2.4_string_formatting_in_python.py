# 파이썬의 문자열 형식화
# 파이썬에서는 복잡한 문자열 출력을 위한 문자열 형식화를 지원한다.
# 형식화 방법에는 % 기호를 사용한 방식과 format 메서드를 사용한 방식, 그리고 f 문자열을 사용하는 방식이 있다.

# % 기호를 사용한 문자열 형식화
# 문자열 뒤에 % 기호를 붙이고 그 뒤에 다른 값을 붙이면 뒤에 붙은 값이 문자열 안으로 들어간다.
# "문자열" % 값
# 문자열의 어느 위치에 ㅏㄱㅄ이 들어가는지를 표시하기 위해 문자열 안에 % 기호로 시작하는 형식지정 문자열(format specification string)을 붙인다.
# %s => 문자열, %d => 정수, %f => 부동소수점 실수
print("내 이름은 %s입니다." % "홍길동")
print("나는 %d살 입니다" % 12)
print("원주율의 값은 %f입니다." % 3.141592)
# 만약 여러개의 값을 문자열 안에 넣어야 한다면 % 기호 뒤에 있는 값을 소괄호로 감싸야 한다.
print("%d 곱하기 %d은 %d이다." % (2, 3, 6))
print("%s의 %s 과목 점수는 %d점이다." % ("철수", "수학", 100))

# exercise 2.4.1
print("%s is %d years old", ("Tom", 13))
a = 10
b = 3
print("%d / %d = %.3f" % (a, b, a / b))

# 고급 형식지정 문자열
# %20s -> 전체 20칸을 차지하는 문자열(공백을 앞에 붙인다.)
# %-10d -> 전체 10칸을 차지하는 숫자(공백을 뒤에 붙인다.)
# %.5f -> 부동소수점의 소수점 아래 5자리까지 표시

print("[%20s]" % "*") # [와 ] 사이에 20칸의 공백이 있다.
print("[%-20s]" % "A") # 20칸의 공백의 앞쪽에 A를 인쇄한다.
print("[%20d]" % 123) # 20칸의 공백의 뒷쪽에 123을 인쇄한다.
print("[%-20d]" % 123) # 20칸의 공백의 앞쪽에 123을 인쇄한다.
x = 1 / 3.0
print("%.5f" % x)
print("[%-20.6f]" % x)

# exercise 2.4.2
a = 3
b = 12
print("'" * 3 + "\n" + "%8d" % a + "\n" + "x" + "%7d" % b + "\n" + "-" * 8 + "\n" + "%8d" % (a * b) + "\n" + "'" * 3)
a = 123456
b = 7890
print("'" * 3 + "\n" + "%10s" % format(a, ',') + "\n" + "+" + "%9s" % format(b, ',') + "\n" + "-" * 10 + "\n" + "%10s" % format((a + b), ',') + "\n" + "'" * 3)