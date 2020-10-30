#문자형 중요


#문자열 생성

str1 = "I am python"
str2 = "Python"
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3),type(str4))
print(len(str1), len(str2), len(str3),len(str4))

# 빈 문자
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

#이스케이프 문자 사용
"""
\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자

"""
escape_str1 = "Do you have a \" retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

#탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

#Raw String
raw_s = r'D:\python\test'
print(raw_s)

#multy line input
#\ 역슬러시 사용하면 쩔어진다
multi_str = \
"""
문자열
멀티라인 입력
테스트
"""


asdf = \
'asdafaf' \
'1234'

print(multi_str)
print(asdf)


# 문자열 연산

str11 = "pytyon"
str22 = "Apple"
str33 = "How are you doing"
str44 = "Seoul! Deajeon! Busan! Jinju"


print(str11 * 3)
print(str11 + str22)
print('y' in str11) # 시퀀스는 in 쓸수 있음
print('z' in str11)
print('P' not in str22)


#문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

#문자열 함수 (upper, isalnum, startswitch, count, endswith, isalpha...)

print("Capitalize : ", str11.capitalize()) #첫글자 대문자화
print("endswith? : ", str22.endswith("s")) #마지막 문자열 확인
print("replace : ", str11.replace("tyon", " good"))
print("sorted : ", sorted(str11))
print("split: ",str44.split('!')) # sep 기준으로 리스트에 저장


#반복(시퀀스)
im_str = "good Boy!"

print(dir(im_str)) #__iter__

for i in im_str:
    print(i)


#슬라이싱 연습

str_s1 = "Nice Python"
str_s2 = "Good Python"
str_s3 = "bad Python"

print(len(str_s1))
print(str_s1[0:3]) # 0 1 2
print(str_s1[5:]) # == [5:11]
print(str_s1[:len(str_s1)]) # [:11]
print(str_s1[:len(str_s1)-1]) # [:10]
print(str_s1[1:9:2]) # 점프하는것
print(str_s1[-5:])
print(str_s1[1:-2])
print(str_s1[::2])
print(str_s1[::-1])

#아스키 코드(또는 유니코드)
a = 'z'
print(ord(a)) #아스키 코드 알아내!
print(chr(122)) #ascii로 읽기
