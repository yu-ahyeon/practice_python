def solution(a, b):
    n = 0
    if a < b:
        for i in range(a, b+1):
            n += i
    elif a > b:
        for i in range(b, a+1):
            n += i
    elif a == b:
        n = a
    return n

x = solution(3, 3)
print(x)

my_list = [2,5,6,7,8]
n = 0
for i in range(len(my_list)):
    if i % 2 == 0:
        n += my_list[i]
my_sum = n
print(my_sum)

easy_sum = sum(my_list)
print(easy_sum)

aa = [1,2,3,4]
if 3 not in aa:
    print("yes")