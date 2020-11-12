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







#
