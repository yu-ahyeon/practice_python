def solution(absolutes, signs):
    n = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            n += absolutes[i]
        else:
            n -= absolutes[i]
    return n

x = solution([4,7,12], [True,False,True])
print(x)
