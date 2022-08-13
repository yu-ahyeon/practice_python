def solution(arr):
    mini = arr[0]
    for a in arr:
        if a < mini:
            mini = a
    arr.remove(mini)
    if arr == []:
        return [-1]
    else:
        return arr
x = solution([10, 11, 12])
print(x)
