from re import A


def solution(array):
    new_array = []
    n = 0
    for a in range(len(array)):
        if a % 2 == 0:
            new_array.append(array[a])
            n += array[a]
    return [new_array, n]
    
x = solution([3, 6, 1, 9, 4])
print(x[0])
print(x[1])

# list에서 중복된 값 제거하는 방법
# set이라는 자료구조를 이용
aa = [1,1,2,3,4,4,5,6]
aa = list(set(aa))
print(aa)

# 숫자를 문자열로 변환
k = 3
t = str(k)
p = int(t)
# 정답은 3입니다.
print("정답은 " + t + "입니다.")

print(1+p)

my_list = ["apple", "banana", "carrot"]

a = [1,2,3,4,5]
b = a*3
print(b)

a = 10000/8
print(a)