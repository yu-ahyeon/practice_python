from itertools import combinations
def solution(nums):
    a = list(combinations(nums, 3))
    b = []
    for i in a:
        b.append(sum(i))
    n = 0
    for j in b:
        if prime(j) == "yes":
            n += 1
    return n

def prime(number):
    for i in range(2, number):
        if number%i == 0:
            return "no"
    return "yes"
x = solution([1, 2, 3, 4])
print(x)