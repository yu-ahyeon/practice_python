def solution(participant, completion):
    participant.sort()
    completion.sort()
    print(participant)
    print(completion)
    return participant[0]
x = solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
print(x)

m = [1, 2, 3, 4]
n = [1, 2, 3]
k = m + n
print(k)