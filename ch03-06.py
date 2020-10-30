#ch03-06
#set 집합
#집합은 (순서x, 중복x)


#선언
a =set()
b =set([1,2,3,4,4,4])
c =set([1,4,5,6])
d = set([1,2,'pen','cap','plate'])
e = {'foo','bar','baz','foo','qux'}
f = {42,'foo',(1,2,3),3.1234}



print(type(a),a, 2 in a)
print(type(b), b)
print(type(a))
print(type(a))
print(type(a))
print(type(a))


t = tuple(b)

print(type(t),t)
print(type(t),t[0],t[1:3])

l = list(c)
l2 = list(e)

print(len(a))
print(len(b))
print(len(c))
print(len(d))


s1 = set([1,2,3,4,5,6])
s2 = set([1,7,3,9,0,6])

print('s1 & s2', s1 & s2)
print('s1 & s2', s1.intersection(s2))

print('s1 & s2', s1| s2)
print('s1 & s2', s1.union(s2))

print('s1 & s2', s1 - s2)
print('s1 & s2', s1.difference(s2))

#중복 원소 확인
print('s1 & s2', s1.isdisjoint(s2))

#부분집합 확인
print('s1 & s2', s1.issubset(s2))
print('s1 & s2', s1.issuperset(s2))

#추가 & 제거

s3 = set([1,2,3,4])

s3.add(5) #추가
print(s3)
s3.remove(5) #x 삭제
print(s3)

s3.discard(3) #x 삭제

print(s3)
s3.discard(7 #에어 안
print(s3)

s3.clear()
print(s3)
