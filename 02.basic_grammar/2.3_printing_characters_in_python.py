print("Hello")
print('한글도 쓸 수 있어요.')

# 문자열 연산
# 문자열도 숫자처럼 덧셈과 곱셈 연산을 할 수 있다.
# 덧셈 연산은 두 문자열을 붙이고 곱셈 연산은 문자열을 반복한다.
print("내 이름은 " + "홍길동" + "입니다.")
print("*" * 10)

# 숫자를 문자열로 바꾸기
# 숫자를 문자열과 더할면 str명령을 써서 숫자를 문자열 자료형으로 바꾸어야 한다.
n = 10
print("별표를 " + str(n) + "번 출력합니다.")
print("*" * n)

# 한 줄 띄우기
# print 명령은 한 번 호출할 때마다 한 줄씩 출력
# "다음 줄 넘기기(line feed) 기호" => \n
print("한 줄 쓰고\n그 다음 줄을 쓴다.")

# 줄을 바꾸지 않고 이어서 출력하기
# print 명령을 여러번 쓰면서 줄은 바꾸지 않고 싶다면 print 명령에 end=""이라는 인수를 추가한다.
print("한 줄 쓰고 ", end="")
print("이어서 쓴다")

# 문자열 값을 가지는 변수
# 변수에는 숫자뿐만 아니라 문자열도 넣을 수 있다.
name = "홍길동"
print("내 이름은 " + name + "입니다.")

mark = '$'
n = 20
print(mark + "기호를 " + str(n) + "번 출력합니다.")
print(mark * n)

# 따옴표를 출력하기
# 파이썬에서 두 가지 종류의 다른 따옴표를 쓸 수 있는 이유는 문자열이 따옴표를 포함하는 경우가 있기 때문
print('둘리가 "호이!"하고 말했어요.')
print("둘리가 '이제 어디로 가지?'하고 생각했어요.")

# 여러 줄의 문자열 출력하기
# "문자"나 '문자' 대신 """여러 줄의 문자열""" 혹은 '''여러 줄의 문자열''' 을 사용
multi_line_string = """
파이썬(영어: Python)은 1991년 프로그래머인
귀도 반 로섬(Guido van Rossum)이 발표한 고급 프로그래밍 언어로,
플랫폼 독립적이며 인터프리터식, 객채지향적, 동적 타이핑(dynamically typed)
대화형 언어이다. 파이썬이라는 이름은 귀도가 좋아하는 코미디 <Monty Python's Flying
Circus>에서 따온 것이다."""

print(multi_line_string)

# exercise 2.3.1
multi_line_string = """
Beautiful is better than ugly
Explicit is better than implicit
Simple is better than complex
Complex is better than complicated
Flat is better than nested
Sparse is better than dense"""

print(multi_line_string)

at = '@'
n = 6

print(at * n + "\n" + at + "    " + at + "\n" + at + "    " + at + "\n" + at + "    " + at + "\n" + at * n)

# 문자열 치환
# 문자열에서 특정 문자를 다른 문자로 바꾸려면 replace 메서드를 사용한다.
print("2020.10.23".replace(".", "-"))
# 문자열의 공백을 없애려면 " " 공백 문자열을 "" 빈 문자열로 바꾸면 된다.
print("word with space".replace(" ", ""))

# exercise 2.3.2
print("2020-12-25".replace("-", ""))