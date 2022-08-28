def solution(arr):
    a = 1
    ah = True
    while ah:
        a += 1
        n = 0
        for i in arr:
            if a % i == 0:
                n += 1
        if n == len(arr):
            ah = False
    return a

x = solution([3, 6, 4, 8, 7])
print(x)