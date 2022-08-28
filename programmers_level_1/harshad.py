def solution(x):
    k = str(x)
    a = []
    for i in k:
        a.append(int(i))
    if x % sum(a) == 0:
        return True
    else:
        return False
x = solution(11)
print(x)