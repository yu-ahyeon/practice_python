def solution(n):
    m = reversed(str(n))
    l = []
    for i in m:
        l.append(int(i))
    return l
x = solution(20104)
print(x)