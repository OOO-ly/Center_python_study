# Ch - 2
#파이썬 완전 기초
#팡다

n = 700

print(n)
print(type(n))

x = y= z = n

print(x,y,z)

#object Ref
#변수 값 할당 상
#1. 타입에 맞는 오브젝트 생성
#2. 값 생성
#3. 콘솔 출력

# 1.

print(300)
print(int(300))
print()

a = 777
b = a

print(a, b)
print(type(a), type(b))
print()

b = 800

print(a, b)
print(type(a), type(b))
print()


# id 확인


print(id(a))
print(id(b))
print(id(a)==id(b))
print()


a = b = 400

print(id(a))
print(id(b))
print(id(a)==id(b))
print()


# 다양한 변수 선언

#camel Case : nuberOfCollegeGraduates -> Method
#pascal Case : NumberOfCollegeFraduates - >Class
#snake Case : number_of_college_graduates -> value
#헝가리안 

# 허용하는 변수 선언 법

age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE = 8
AGE = 7


#예약어는 변수명으로 불가능

"""
False def if raise
None del import return
Ture elif in try
and else is while
as except lambda with
assert finally nonlocal yield
break for not
class from or
continue global  pass
"""
