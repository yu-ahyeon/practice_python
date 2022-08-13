def solution(answers):
    a = [1,2,3,4,5]*2000
    b = [2,1,2,3,2,4,2,5]*1250
    c = [3,3,1,1,2,2,4,4,5,5]*1000
    l = 0
    m = 0
    n = 0
    for i in range(len(answers)):
        if answers[i] == a[i]:
            l += 1
        if answers[i] == b[i]:
            m += 1
        if answers[i] == c[i]:
            n += 1
    my_list = [l, m, n]
    my_max = max(my_list)
    answer = []
    for j in range(len(my_list)):
        if my_list[j] == my_max:
            answer.append(j + 1)
    return answer

x = solution([1,3,2,4,2])
print(x)

