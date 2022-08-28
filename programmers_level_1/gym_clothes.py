def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    a = len(reserve)
    for i in range(1, n+1):
        if i not in lost:
            if i not in reserve:
                a += 1
    for j in range(1, n+1):
        if j in lost:
            if j in reserve:
                lost.remove(j)
                reserve.remove(j)
    for k in lost:
        if k-1 in reserve:
            a += 1
            reserve.remove(k-1)
        elif k+1 in reserve:
            a += 1
            reserve.remove(k+1)
    return a
# x = solution(20, [2, 4, 5], [3, 6])
# print(x)
    lost.sort()
    reserve.sort()
    a = len(lost)
    for i in lost:
        if i in reserve:
            a -= 1
            lost.remove(i)
            reserve.remove(i)
    for j in lost:
        if j-1 in reserve:
            a -= 1
            reserve.remove(j-1)
        elif j+1 in reserve:
            a -= 1
            reserve.remove(j+1)         
    return n-a

x = solution(5, [2, 4], [1, 3, 5])
print(x)
