def solution(lottos, win_nums):
    n = 0
    for i in lottos:
        if i in win_nums:
            n += 1
    l = n
    if 0 in lottos:
        l += lottos.count(0)
    if n == 6:
        return [1, 1]
    elif n == 5:
        n_rank = 2
    elif n == 4:
        n_rank = 3
    elif n == 3:
        n_rank = 4
    elif n == 2:
        n_rank = 5
    else:
        n_rank = 6
    if l == 6:
        l_rank = 1
    elif l == 5:
        l_rank = 2
    elif l == 4:
        l_rank = 3
    elif l == 3:
        l_rank = 4
    elif l == 2:
        l_rank = 5
    else:
        l_rank = 6
    return [l_rank, n_rank]
x = solution([0, 0, 0, 0, 0, 0], [31, 10, 45, 1, 6, 19])
print(x)
