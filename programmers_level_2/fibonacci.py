def solution(n):
    a = [0, 1]
    for i in range(2, n+1):
        my_result = a[i-2] + a[i-1]
        a.append(my_result)
    my_answer = a[n] % 1234567
    return my_answer
x = solution(5)
print(x)