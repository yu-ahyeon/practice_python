def solution(people, limit):
    boats = 0
    people.sort()
    small_man = 0
    big_man = len(people) - 1
    while small_man <= big_man:
        if people[small_man] + people[big_man] > limit:
            big_man -= 1
            boats += 1
        else:
            big_man -= 1
            small_man += 1
            boats += 1
    return boats