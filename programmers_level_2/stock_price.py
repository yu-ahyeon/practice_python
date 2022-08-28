def solution(prices):
    my_result = []
    for i in range(len(prices)):
        second = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                second += 1
            elif prices[i] > prices[j]:
                second += 1
                break
        my_result.append(second)
    return my_result
x = solution([1,4,3,2,3,6,4,2])
print(x)