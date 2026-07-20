#사칙연산자

#print(2 + 3)

#print(2 - 3)

#print(2 * 3)

#print(2 / 3)

#print(1 + 3 * 4)

#복합대입연산
#+=
#-=
#*-
#/-
#%=
#//=
#**=

num = 1
num = num + 1
print(num)

num += 1
print(num)
num //= 1
print(num) 
num /= 1
print(num)
num *= 1
print(num)
num -= 1
print(num)

#다중 할당
num1, num2, num3 = 1, 2, 1
print(num1,num2,num3)

print(num1 == num2)
print(num1 != num2)
print(num1 != num3)
print(num1 == num3)

print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)

print("가방" < "가족")
print([1, 2] < [1, 3])
#print([1, 3] < "한글") 

#3 in [1, 2, 3, 4]
print(3 in [1, 2, 3, 4])
#5 in [1, 2, 3, 4]
print(5 in [1, 2, 3, 4])

print(1 == None)
print(1 is None)

#논리 연산자
#and or not

li = [1, 2, 3, 4]
print(5 not in li) 
print(1 is not 1.0)
print((1 + 3)* 4)

# 1. 사칙연산을 전부 활용해서 10(또는 10.0)이 나오도록 산술연산자를 사용
print((5 + 2 - 3) * 5 / 2)
# 2. 나머지 연산자와 몫 연산자를 이용해서 5의 결과가 나오도록 산술연산자를 사용
print(11 // 2 % 7)
# 3. 3 ** 2 ** 2 에 대한 내용을 '*' 연산자와 '()' 연산자를 이용하여 만들기
print(3 * 3 * 3 * 3)
# 4. 1의 값을 가진 num변수를 복합대입연산자를 이용하여 +3, -2, *3, /2를 했을 때의 결과를 출력
num = 1
num + 3
print(num)
num - 2
print(num) 
num * 3
print(num)
num / 2
print(num)
# 5. 102와 201의 값을 이용하여 True가 나오도록 비교 연산자(==,!=,>,<,>=,<=)를 이용하여 작성

# 6. 102 + 101 < 20 + 1의 결과가 무엇이 나오고, 왜 그렇게 나오는지 적을것

# 7. True and True or False and True or True or False and True 의 결과는?
print(True and True or False and True or True or False and True)




 


 
 



