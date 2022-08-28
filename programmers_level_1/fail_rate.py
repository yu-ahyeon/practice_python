def solution(N, stages):
    n = 0
    rates = []
    for i in range(1, N+1):
        if len(stages)-n == 0:
            i_rate = 0
        else:
            i_rate = stages.count(i)/(len(stages)-n)
        rates.append([i, i_rate])
        n += stages.count(i)
    rates.sort(key=lambda x: (-x[1], x[0]))
    a = []
    for j in rates:
        a.append(j[0])
    return a
x = solution(5, [2, 1, 2, 2, 2, 4, 3, 3])
print(x)