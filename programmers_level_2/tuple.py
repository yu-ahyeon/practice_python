def solution(s):
    if s[0] == ")":
        return False
    if s[-1] == "(":
        return False
    if s.count("(") == s.count(")"):
        return True
    else:
        return False
x = solution("(())(")
print(x)