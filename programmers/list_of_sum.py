def solution(numbers):
    my_result = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            a = numbers[i] + numbers[j]
            my_result.append(a)
    my_result = list(set(my_result))
    my_result.sort()
    return my_result
x = solution([5,0,2,7])
print(x)