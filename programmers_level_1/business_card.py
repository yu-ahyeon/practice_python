def solution(sizes):
    a = []
    b = []
    for i in sizes:
        a.append(max(i))
        b.append(min(i))
    return max(a)*max(b)
x = solution([[60, 50], [30, 70], [60, 30], [80, 40]])
print(x)