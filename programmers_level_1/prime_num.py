from itertools import combinations
def solution(nums):
    
    answer = 0
    for element in b:
        if is_prime(element) == "yes":
            answer += 1
    return answer

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return "no"
    return "yes"

x = solution([1,2,7,6,4])
print(x)