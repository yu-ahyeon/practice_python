def solution(n):
    my_list = []
    for i in range(1,n+1):
        if n % i == 0:
            my_list.append(i)
    my_result = sum(my_list)
    return my_result
x = solution(12)
print(x)
