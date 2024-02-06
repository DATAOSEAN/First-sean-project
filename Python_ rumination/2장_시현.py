# 문제1.
number = {'국어':80, '영어':75, '수학':55}
answer = 0
for i in number.values():
    answer = answer + i
result = answer / len(number)
print(result)

# 문제2.
n = 13
if i % 2 == 0:
    print("'{}'은 짝수입니다.".format(n))
else:
    print("'{}'은 홀수입니다.".format(n))

# 문제3.
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:14]
print(yyyymmdd)
print(num)

# 문제4.
pin = "881120-1068234"
print(pin[7])

# 문제 5.
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

# 문제 6.
a = [1,3,5,4,2]
a.sort()
a.reverse()
a

# 문제 7.
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
result

# 문제 8. 미해결
a = 1, 2, 3
b = 4
c = a + b
c

# 문제 9. 가변형 자료형인 리스트는 key로 부적합하다.
a = dict()
a[('a',)] = 'python'
a

# 문제 10. 미해결
a = {'A':80, 'B':80, 'C':70}
result = a.pop(['B'])
result

# 문제 11. 미해결
a = [1,1,1,2,2,3,3,3,4,4,5]
a.set()
a

# 문제 12. 미해결
a = b = [1,2,3] # 이때 두 개의 변수가 생성된다.
a[1] = 4 # a변수만 인덱스를 이용해 값을 변경한다.
print(a) # a는 1,4,3
print(b) # b는 그대로 나올 것이다. 틀렸당^^
