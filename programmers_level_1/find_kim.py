def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "kim":
            j = str(i)
            return "김서방은 j에 있다"

x = solution(["Jane", "kim"])
print("김서방은", x, "에 있다.")