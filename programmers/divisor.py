def solution(left, right):
    my_list = []
    a = 1
    while a**2 <= right:
        my_list.append(a**2)
        a = a + 1
    n = 0
    for i in range(left, right+1):
        if i in my_list:
            n -= i
        else:
            n += i
    return n
x = solution(24, 27)
print(x)