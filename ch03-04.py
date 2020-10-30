#ch03-04
#튜플
#리스트와 비교 중요
#튜플 자료형(순서ㅇ,중복ㅇ,수정x,삭제x) # 불변


# 선언
a = ()
b = (1,)
c = (11,12,13,14)
d = (100,1000,'a','b','c')
e = (100,1000,('a','base','c'))

print('>>>>')
print('d - ',d[1])
print('d - ',d[0] + d[1]+ d[1])
print('d - ',d[-1])
print('e - ',e[-1])
print('e - ',e[-1][1])
print('e - ',list(e[-1][1]))

# 수정

#d[0] = 1500
print('d - ',d[0:3])
print('d = ',d[2:])
print('e = ',e[2][1:3])

#튜펀 연산

print('c + d', c+d )
print('c + d', c*3 )

#튜플 함수

a = (5,2,3,1,4)
print('a - ',a)
print('a - ',a.index(3)) # x가 어디 있는가?
print('a - ',a.count(2)) # x의 개쇼ㅜ

#팩킹 언팩킹

t = ('foo','var','vax','qux')
print(t)
print(t[0])
print(t[-1])


(x1, x2, x3, x4) = t
print(type(x1),type(x2),type(x3),type(x4))
print(x1,x2,x3,x4)


x1, x2, x3 = t1
x4, x5 = 4,5


#print(type(a),type(b))
