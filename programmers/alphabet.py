def solution(s, n):
    answer = ""
    for element in s:
        print("ele", element)
        if element == " ":
            answer += element
        elif ord(element) <= 90:
            if ord(element) + n <= 90:
                answer += chr(ord(element) + n)
            else:
                answer += chr(ord(element) + n - 26)
        else:
            if ord(element) + n <= 122:
                answer += chr(ord(element) + n)
                # print(chr(ord(element) + n))
            else:
                answer += chr(ord(element) + n - 26)
                # print(chr(ord(element) + n - 26))
    return answer

a = solution("a B z", 4)
print(a)
