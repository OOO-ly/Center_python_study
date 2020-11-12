#Chapter 04-1
#파이썬 제어문
#IF 실습

#기본 형식
print(type(True)) #0이 아닌 수,
print(type(False)) # 0,"". [], (), {}

#에1

if 'a':
    print('Bad')
else:
    print('Good')


#Ex 2
if False:
    print('Bad!')
else:
    print('Good')

#Ex3
#관게 연산자
# > , >= , < , <= , == < !=

x = 15
y = 10

#양변이 같을 경우 참
print(x == y)

#양번이 다를 때 참
print(x != y)

#왼쪽이 클 때 참
print(x > y)
#왼쪽이 크거나 같을 때 참
print(x >= y)
#오른쪽이 클 때 참
print(x < y)
#오른쪽이 크거나 같을 때 참
print(x <= y)


city = ''

if city:
    print(city)
else:
    print('city is empty')

city2 = 'jeju'

if city2:
    print('asdasd',city2)
else:
    print('city is : ',city2)


#논리연산자(중요)
#and , or , not

a = 75
b = 40
c = 10

print('and : ', a > b and b > c)# a > b > c
print('or : ', a > b or b > c)# a > b > c
print('not', not a > b )
print('not',not b > c)
print(not True)
print(not False)


#산술, 관계, 논리 우선순위
#산술 > 관계 > 논리
print('e1 : ',3+12 > 7+3)
print('e2 : ',5+10 * 3 > 7+ 7+3 *20)
print('e3 : ',5+10 * 3 and 7+ 7+3 *20 == 10)
print('e4 : ',5+10 * 3 and not 7+ 7+3 *20 == 10)

score1 = 90
score2 = 'A'

#복수의 조건이 모두 참일 경우에 실행
if score1 >= 90 and score2 == 'A':
    print('Pass')
else:
    print('Fail')

id1 = 'vip'
id2 = 'admin'
grade2 = 'Platinum'

if id1 == 'vip' and grade2 == 'Platinum':
    print('플래티넘  vip 입장')

if id2 == 'admin' and id1 == 'vip':
    print('관리자 입장')


#예6 다중조건문

num = 90

if num >= 90:
    print('Grade : A')
elif num >= 80:
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
else:
    print('과락')

#중첩 조건문

grade = 'A'
total = 95

if grade =='A':
    if total >= 90:
        print('장학금 100%')
    elif total >= 80:
        print('장학금 80%')
    else:
        print('장학금 50%')
else:
    print('장학금 없음')


#in , not in

q = [10,20,30]
w = {70,80,90,100}
e = {"name" : "Lee", "city" : "jeju", "grade": 'A'}
r = (10,12, 14)

print(15 in q)
print(90 in w)
print(2 not in r )
print("name" in e)
print("jeju" in e)
print("jeju" in e.values())
