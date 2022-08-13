def solution(n):
    if int(n**0.5) == n**0.5:
        my_result = int((n**0.5 +1)**2)
    else:
        my_result = -1
    return my_result

a = solution(121)
print(a)