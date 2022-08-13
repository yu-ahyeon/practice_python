def solution(numbers):
    n = 0
    for a in range(10):
        if a not in numbers:
            n += a
    return n
x = solution([5,8,4,0,6,7,9])
print(x)