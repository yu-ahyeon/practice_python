def solution(nums):
    n = len(set(nums))
    if n > len(nums)//2:
        my_result = len(nums)//2
    else:
        my_result = n
    return my_result
x = solution([3,3,3,2,2,2])
print(x)