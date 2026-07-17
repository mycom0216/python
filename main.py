print("Hello, World!")
a = 5
b = 10
print(a, b)
greet = "Hello, World!"
num_str = str(a + b)
print(greet.replace("World", "Python"))
print(type(num_str))

# print(greet.replace("World", "Python"))
# print(type(num_str))
print(f"num_str의 변수값은 {num_str}입니다.")
greet_the_great_name = "반재영"
print(greet_the_great_name)

tuple0 = (1, 2, 3)
tuple1 = (1.1, 1.2, 1.3)
tuple2 = ('안녕', '하세요')
tuple3 = (1, 1.1, '안녕') 
tuple4 = (1, )
tuple5 = (tuple0, tuple1)
tuple6 = ((1, 2, 3), (1.1, 1.2, 1.3))
tuple7 = ((1, ), (1, 2), (1, 2, 3))

tu1 = (1, 2, 3, 4, 5) #0 1 2 3 4
print(tu1[0:5:2])

print(tu1[::2]) ## 이 방법으로도 1,3,5 출력가능

print(tu1[:3]) 

print(tu1[2:])


str1 = "안녕하세요" 
print(str1[0:2])

print("언" + str1[1:]) ##튜플은 수정불가

tu2 = (1, 1, 2, 3, 4, 4, 5)

print(tu2.count(2)) ##count는 끝까지 찾음

print(tu2.index(3))

print(tu2.index(4))

L1 = []
L2 = [1]
L3 = [1, 2, 3]
L4 = [[1], [2], [3]]
L5 = [L3, L3, L3]
L6 = ["string", 1, 1.1]
L7 = list((1, 2, 3))

print(L3, L6, L7)

Li1 = [1, 2, 3, 4, 5]
print(Li1[0])
print(Li1[0:3])

Li1 = [1, 2] + [3, 4]
print(Li1)

print(Li1.extend([5, 6])) ##값을 반환하지않음, 출력 시 none
print(Li1)


Li1 = [1, 2, 3]
Li1.append([4])
print(Li1)

Li1 = [1, 2, 4, 5]
Li1.insert(2, 3)
print(Li1)