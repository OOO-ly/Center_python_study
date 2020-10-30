str123 = "hello! heeeee! eeee"

temp =sorted(str123)
#temp = str.split('!')

#print(type(str123))
#print(type(temp))
#print(temp)

#temp2 = str(temp)

temp2 = []

while temp:
    temp2 += temp.pop()


print(temp2)
#print(type(str(temp)))
print(type(temp2))
#print(temp2)
