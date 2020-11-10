#if문





a = 90
b = 70
c = 30


print('not', not a > b)
print('not',not b > c)
print('not')


print(not False)
print(3+12 > 7+3)
print(5 + 10 * 3> 7 + 3 == 10)
print(5 + 10 > 3 and 7 + 3 == 10)
print(5 +10 > 0 and not 7 + 3 == 10)

score1 = 90
score2 = 'a'

if score1 >= 90 and score2 == 'A' or 'a':
    print('Pass')
else:
    print('Fail')


# 예5
num = 80


id1 = 'vip'
id2 = 'admin'
grade = 'platunum'

if id1 == 'vip' or id2 == 'admin':
    print('관리자 입장')


if id2 == 'admin' and grade == 'platunum':
    print('최상위 관리자')


#에6
#다중 조건문

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
total = 80

if grade == 'A':
    if total >= 90:
        print('장학금 100%')
    elif total >= 80:
        print('장학금 80%')
    else:
        print('장학금 50%')
else:
    print('장학금 없음')
