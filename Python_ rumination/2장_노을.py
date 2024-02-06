#Q1.
score = [80, 75, 55]
b = sum(score) / len(score)
b

#Q1.
score = [80, 75, 55]
b = sum(score) / len(score)
b

#Q3.
pin = "881120-1068234"
yyyymmdd = "19"+ pin[:5]
num = pin[7:]
print(yyyymmdd)
print(num)

#Q4.
print(pin[7])

#Q5.
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

#Q6.
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

#Q7.
a = ["Life", "is","too","short"]
result = " ".join(a)
print(result)

#Q8.
a = (1, 2, 3)
a = a + (4,) # 하나의 요소만 있는 튜플은 뒤에 콤마 붙여야 함
print(a)

#Q9.
a = dict()
a
a['name'] = 'python'
a[('a',)] = 'python'
#a[[1]] = 'python'  딕셔너리의 키는 immutable 값을 넣어야 함. 
# [1]은 리스트, mutable
a[250] = 'python'
a

##Q10.
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

#Q11.
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
# b = list(set(a)) #위의 두줄 지우고 요것만 써도 가능
print(b)

#Q12.
a = b = [1, 2, 3]
a[1] = 4
print(b) 
#변수는 값[1, 2, 3]이 저장된 주소?를 저장하기 때문에 'a=b'에서 같은 주소가
#저장되어 리스트의 하나의 요소를 바꾸더라도 다 같이 바뀜
