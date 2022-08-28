def solution(s):
    arranged = sorted(list(s), reverse = True)
    my_result = "".join(arranged)
    return my_result
x = solution("Zbcdefg")
print(x)