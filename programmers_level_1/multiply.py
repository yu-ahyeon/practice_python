def solution(a, b):
    n = 0
    for i in range(len(a)):
        n += a[i]*b[i]
    return n
x = solution([1,2,3,4], [-3,-1,0,2])
print(x)