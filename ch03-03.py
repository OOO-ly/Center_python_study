#ch 03 - 3
#파이썬  리스트
#자료구조에서 중요
#리스트 자료형(순서o, 중복o 수정ㅇ 삭제ㅇ)

#선언
a = []
b = list()
c = [70,75,80,85]
print(len(c))
d= [1000, 10000, 'ace', 'B', 'c']
e= [1000, 10000, ['ace', 'B', 'c']]
f= [21.42, 'foo',3,4,False,3.14]


print('>>>>>')
print('d - ',type(d),d)
print('d - ',d[1])
print('d - ',d[0] + d[1] + d[1])
print('d - ',d[-1])
print('e - ',e[-1][1])
print('e - ',list(e[-1][1]))


print('>>>>')
print('d - ',d[0:3])
print('d - ',d[2:])
print('d - ',e[-1][1:3])

print('>>>>')
print('C + D ', c +d)
print('c * 3 ',c * 3)
print("Test + c[0]", 'Test'+ str(c[0]))


#값비교
print( c == c[:3] + c[3:])
print(c[3:])
print(c[:3])


temp = c
print(temp,c)
print(id(temp))
print(id(c))

#리스트 수정 , 삭제

print('>>>>')
c[0] = 4
print('c - ',c)
print('c - ',c[1:2])
c[1:2] = ['a','b','c'] # ['a','b','c']
print('c - ',c)
c[1] = ['a','b','c'] # == [['a','b','c']]
print('c - ',c)
c[1:3] = []
print('c - ',c)
del c[2] # 삭제
print('c - ',c)

#리스트 함수
a = [5,2,3,1,4]
print('a - ',a)
a.append(10) # 삽입
print('a - ',a)
a.sort() #오름차순
print('a - ',a)
a.reverse() #역 순
print('a - ',a)
print('a - ',a.index(3), a[3])
a.insert(2,7) # x에 y를 삽입
print('a - ',a)
a.reverse()
print('a - ',a)
a.remove(10) #x인 값을 삭제
print('a - ',a)

print('a - ',a)
print('a - ',a.pop())
print('a - ',a)
print('a - ',a.pop()) #맨 뒤에 값을 pop stack
print('a - ',a)
print('a - ',a.count(1)) #x값을 카운팅

ex = [8,9]
a.extend(ex)
print('a - ',a)

#삭제 : remove , pop , del

while a:
    data = a.pop()
    print(data)
