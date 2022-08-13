def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "kim":
            return i

x = solution(["Jane", "kim"])
print("김서방은", x,"에 있다.")