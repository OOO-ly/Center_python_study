#ch03-05
#딕셔너리

a = {'name' : 'kim','ph':'010','bir' : "87" }
b = { 0 : 'hello'}
c = { 'arr' : [1,2,3,4]}
d = {
'name' : 'kim',
'ph':'010',
'age' : 33,
'bir' : "87",
'stat' : True
}

e = dict([
    (    'name' , 'kim'),
    (    'ph','010'),
    (    'age' , 33),
    (    'bir' , "87"),
    (  'stat' , True )

])

f= dict(
    Name='Nice',
    City='Seoul',
    Age=33,
    Grade='A',
    stat=True
)


print('a - ',type(a),a)
print('b - ',type(b),b)
print('c - ',type(c),c)
print('d - ',type(d),d)
print('e - ',type(e),e)
print('f - ',type(f),f)


print('a - ',a['name']) # 에러 발생
print('a - ',a.get('name')) #키가 없으면 none
print('b - ',b[0])
print('b - ',b.get(0))
print('c - ',c['arr'])
print('c - ',c.get('name'))




#딕셔너리 추가
a['addr'] = 'Seoul'
print('a- ',a)
a['rank'] = [1,2,3]
print('a- ',a)


print('a- ',len(a))
print('a- ',len(b))
print('a- ',len(c))
print('a- ',len(d))

#dict_keys, dict_values, dict_items : 반복분 __iter__에서 사용 가능


print('a- ',a.keys())
print('a- ',list(a.keys())) # 키만 리스트로 형변환 해서 받을 수 있다

print('a- ',a.values()) # 값만

print('a- ',a.items()) #키와 값 모두# 튜플로 하나의 키와 밸류가 저장된다


print('a- ',a.pop('name'))
print('a- ',a)

print('a- ',a.popitem())
print('a- ',a.popitem())
print('a- ',a.popitem())
print('a- ',a.popitem())
print('a- ',a) #사전은 순서가 없으니 추천기 만들ㄱ때 쓸수 있다고 하는데 회의 필요

print('f - ','Age' in f)#딕셔너리에 있는지 없는지? 포함여부
print('f - ','City' in f)

#수정
f['test'] = 'test_dict'
print('f - ',f)

f['addr'] = 'dj'
print('f - ',f)

f.update(agag=123123)
print('f - ',f)

temp={'addr':'bubu'}

f.update(temp)
print('f - ',f)
