#chapter03-1
# 숫자형

#파이썬 지원 자료형

"""

int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전

"""

str1  = "python"
bool = True
str2 = 'Anaconda'
float_v = 10.0 # 10 != 10.0
int_v = 7
list = [str1, str2]
dict = {
"name" : "Machine Learning",
"version": 2.0
}
tuple = (7, 8, 9)
set = {7, 8, 9}

print(type(str1))
print(type(bool))
print(type(str2))

print(type(float_v))
print(type(int_v))
print(type(list))

print(type(dict))
print(type(tuple))
print(type(set))


# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지

abs(x) : 절대값
pow(x, y) / x ** y :  x의 y 제곱


"""
#정수
i = 77
i2 = -14
big = 77777777777777777777777777777777777777777777777777777777

print(i)
print(i2)
print(big)

#실수
f1 = 0.999999
f2 = 3.14592
f3 = -3.9
f4 = 3 / 9


print(f1)
print(f2)
print(f3)
print(f4)
print()

#연산 실습

i1 = 39
i2 = 939
big1 = 999999999
big2 = 312345551
f1 = 1.234
f2 = 3.393

print(">>>>>>+")
print("i1 + i2 : ",i1 + i2)
print("f1 + f2 : ",f1 + f2)
print("big1 + big2 : ",big1 + big2)



print(">>>>>>-")
print("i1 + i2 : ",i1 - i2)
print("f1 + f2 : ",f1 - f2)
print("big1 + big2 : ",big1 + big2)


print(">>>>>>*")
print("i1 + i2 : ",i1 * i2)
print("f1 + f2 : ",f1 * f2)
print("big1 + big2 : ",big1 * big2)


print(">>>>>>/")
print("i1 + i2 : ",i1 / i2)
print("f1 + f2 : ",f1 / f2)
print("big1 + big2 : ",big1 / big2)

print(">>>>>>//")
print("i1 + i2 : ",i1 // i2)
print("f1 + f2 : ",f1 // f2)
print("big1 + big2 : ",big1 // big2)


print(">>>>>>%")
print("i1 + i2 : ",i1 % i2)
print("f1 + f2 : ",f1 % f2)
print("big1 + big2 : ",big1 % big2)


# 형변환 실습

a = 3.
b = 6
c = .7
d = 12.7


print(type(a), type(b), type(c), type(d))

# 형변환

print(float(b))
print(int(c))
print(int(d))
print(int(False)) # True False 대문자 맞춰줘야함
print(float(True))
print(complex(3))
print(complex('3')) # 문자형 -> 숫자형 -> 복소수
print(complex(False))

#수치 연산 함수

print(abs(-7))
x, y = divmod(100, 8) # 나누고 몫 나머지 바로 할당
print(x, y)

print(pow(5,3), 5**3 ,sep="#")

#외부 모듈(package)
import math

print(math.ceil(5.1))
print(math.pi)



#암묵적 형변환
#모두 float로 변환됨
#print(type(i1 + f1))
#print(type(f1 + i1))
